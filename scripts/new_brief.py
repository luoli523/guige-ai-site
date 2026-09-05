#!/usr/bin/env python3
"""把 bot 产出的 JSON 转成一篇每日简报，校验通过后落盘、构建、提交。

用法：
    cat brief.json | python3 scripts/new_brief.py                 # 校验并写入
    cat brief.json | python3 scripts/new_brief.py --check         # 只校验，不写
    cat brief.json | python3 scripts/new_brief.py --commit --push # 写入并推送

退出码（bot 靠这个判断该怎么办）：
    0  成功
    1  输入或校验失败    —— 修正 JSON 后重试
    2  当天简报已存在    —— 加 --force 才覆盖
    3  Hugo 构建失败     —— 已回滚，内容有问题
    4  git 操作失败      —— 内容已落盘，需人工介入
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Asia/Shanghai")
REPO = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO / "content" / "daily"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MIN_ITEMS = 2      # 少于这个条数视为采集失败，拒绝发布
MAX_TAGS = 8


class Invalid(Exception):
    """输入不合规。"""


def fail(code, msg):
    print(f"错误：{msg}", file=sys.stderr)
    sys.exit(code)


# ── 校验 ────────────────────────────────────────────────────────────

def validate(data):
    """校验并归一化 bot 的 JSON，返回补全后的 dict。"""
    if not isinstance(data, dict):
        raise Invalid("顶层必须是 JSON 对象")

    # date
    raw_date = data.get("date") or date.today().isoformat()
    if not DATE_RE.match(str(raw_date)):
        raise Invalid(f"date 必须是 YYYY-MM-DD，收到 {raw_date!r}")
    try:
        d = date.fromisoformat(raw_date)
    except ValueError:
        raise Invalid(f"date 不是合法日期：{raw_date!r}")

    today = datetime.now(TZ).date()
    if d > today + timedelta(days=1):
        raise Invalid(f"date {d} 在未来太远（今天是 {today}），多半是模型算错了日期")

    # sections
    sections = data.get("sections")
    if not isinstance(sections, list) or not sections:
        raise Invalid("sections 必须是非空数组")

    total_items = 0
    clean_sections = []
    for i, sec in enumerate(sections):
        if not isinstance(sec, dict):
            raise Invalid(f"sections[{i}] 必须是对象")
        heading = str(sec.get("heading", "")).strip()
        if not heading:
            raise Invalid(f"sections[{i}].heading 不能为空")

        items = sec.get("items")
        if not isinstance(items, list):
            raise Invalid(f"sections[{i}].items 必须是数组")

        clean_items = []
        for j, item in enumerate(items):
            if not isinstance(item, dict):
                raise Invalid(f"sections[{i}].items[{j}] 必须是对象")
            title = str(item.get("title", "")).strip()
            body = str(item.get("body", "")).strip()
            if not title:
                raise Invalid(f"sections[{i}].items[{j}].title 不能为空")
            if not body:
                raise Invalid(f"sections[{i}].items[{j}].body 不能为空（{title}）")

            url = str(item.get("url", "")).strip()
            if url and not url.startswith(("http://", "https://")):
                raise Invalid(f"sections[{i}].items[{j}].url 不是合法链接：{url!r}")

            clean_items.append({"title": title, "body": body, "url": url})

        if clean_items:                      # 空小节直接丢掉，不渲染空标题
            clean_sections.append({"heading": heading, "items": clean_items})
            total_items += len(clean_items)

    if total_items < MIN_ITEMS:
        raise Invalid(
            f"只有 {total_items} 条内容，少于下限 {MIN_ITEMS} 条。"
            "宁可今天不发，也不要发一篇空简报"
        )

    # tags / sources：去重保序
    def dedup(key, limit=None):
        raw = data.get(key) or []
        if not isinstance(raw, list):
            raise Invalid(f"{key} 必须是数组")
        seen, out = set(), []
        for x in raw:
            s = str(x).strip()
            if s and s not in seen:
                seen.add(s)
                out.append(s)
        if limit and len(out) > limit:
            out = out[:limit]
        return out

    return {
        "date": d,
        "title": str(data.get("title") or f"{d.isoformat()} AI 要闻").strip(),
        "summary": str(data.get("summary") or "").strip(),
        "tags": dedup("tags", MAX_TAGS),
        "sources": dedup("sources"),
        "intro": str(data.get("intro") or "").strip(),
        "sections": clean_sections,
        "total_items": total_items,
    }


# ── 渲染 ────────────────────────────────────────────────────────────

def render(b):
    q = json.dumps          # 用 JSON 字符串转义，避免引号/冒号把 YAML 弄坏

    fm = [
        "---",
        f"title: {q(b['title'], ensure_ascii=False)}",
        f"date: {b['date'].isoformat()}T08:00:00+08:00",
    ]
    if b["summary"]:
        fm.append(f"summary: {q(b['summary'], ensure_ascii=False)}")
    if b["tags"]:
        fm.append("tags: [" + ", ".join(q(t, ensure_ascii=False) for t in b["tags"]) + "]")
    if b["sources"]:
        fm.append("sources: [" + ", ".join(q(s, ensure_ascii=False) for s in b["sources"]) + "]")
    fm.append("---")

    body = []
    if b["intro"]:
        body += ["", b["intro"]]

    for sec in b["sections"]:
        body += ["", f"## {sec['heading']}", ""]
        for item in sec["items"]:
            line = f"- **{item['title']}** — {item['body']}"
            if item["url"]:
                line += f" [来源]({item['url']})"
            body.append(line)

    return "\n".join(fm) + "\n" + "\n".join(body).rstrip() + "\n"


# ── 外部命令 ────────────────────────────────────────────────────────

def run(cmd, **kw):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, **kw)


def hugo_build():
    """构建一次，确认新内容不会把站点弄挂。Hugo 不在就跳过。"""
    probe = run(["hugo", "version"])
    if probe.returncode != 0:
        print("提示：没找到 hugo，跳过构建校验", file=sys.stderr)
        return True
    r = run(["hugo", "--minify", "--quiet"])
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
        return False
    return True


# ── 主流程 ──────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="生成并提交一篇每日 AI 要闻简报")
    ap.add_argument("--json", type=Path, help="读取 JSON 文件（默认从 stdin 读）")
    ap.add_argument("--check", action="store_true", help="只校验并打印结果，不写文件")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的当天简报")
    ap.add_argument("--commit", action="store_true", help="写入后自动 git commit")
    ap.add_argument("--push", action="store_true", help="commit 后推送到 origin main")
    args = ap.parse_args()

    raw = args.json.read_text(encoding="utf-8") if args.json else sys.stdin.read()
    if not raw.strip():
        fail(1, "没有收到任何输入")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        fail(1, f"JSON 解析失败：{e}")

    try:
        brief = validate(data)
    except Invalid as e:
        fail(1, str(e))

    text = render(brief)
    path = CONTENT_DIR / f"{brief['date'].isoformat()}.md"

    if args.check:
        print(text)
        print(
            f"--- 校验通过：{brief['total_items']} 条内容 / "
            f"{len(brief['sections'])} 个小节 → {path.relative_to(REPO)}",
            file=sys.stderr,
        )
        return

    existed = path.exists()
    if existed and not args.force:
        fail(2, f"{path.relative_to(REPO)} 已存在。确认要覆盖就加 --force")

    backup = path.read_text(encoding="utf-8") if existed else None
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"已写入 {path.relative_to(REPO)}（{brief['total_items']} 条）")

    if not hugo_build():
        # 构建挂了就还原，别把坏内容留在仓库里
        if backup is None:
            path.unlink()
        else:
            path.write_text(backup, encoding="utf-8")
        fail(3, "Hugo 构建失败，已回滚")

    if not (args.commit or args.push):
        return

    msg = f"content: {brief['date'].isoformat()} AI 要闻（{brief['total_items']} 条）"
    r = run(["git", "add", str(path)])
    if r.returncode != 0:
        fail(4, f"git add 失败：{r.stderr}")

    r = run(["git", "commit", "-m", msg])
    if r.returncode != 0:
        if "nothing to commit" in (r.stdout + r.stderr):
            print("内容与上次完全相同，无需提交")
            return
        fail(4, f"git commit 失败：{r.stderr or r.stdout}")
    print(f"已提交：{msg}")

    if args.push:
        r = run(["git", "push", "origin", "main"])
        if r.returncode != 0:
            fail(4, f"git push 失败：{r.stderr}")
        print("已推送到 origin/main，Actions 会自动构建发布")


if __name__ == "__main__":
    main()
