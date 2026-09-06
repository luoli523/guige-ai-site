#!/usr/bin/env python3
"""把 bot 产出的深读 JSON 转成每日 Markdown，校验通过后落盘、构建、提交。

用法：
    cat brief.json | python3 scripts/new_brief.py                 # 校验并写入
    cat brief.json | python3 scripts/new_brief.py --check         # 只校验，不写
    cat brief.json | python3 scripts/new_brief.py --commit --push # 写入并推送

退出码：
    0  成功
    1  输入或校验失败
    2  当天报告已存在（加 --force 覆盖）
    3  Hugo 构建失败（已回滚）
    4  git 操作失败（内容可能已落盘）
"""

from __future__ import annotations

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
MAX_TAGS = 8
MIN_BODY_CHARS = 2500
REQUIRED_SEMANTICS = (
    ("执行摘要", ("执行摘要",)),
    ("主线/深度", ("主线", "深度解析")),
    ("来源", ("来源", "延伸阅读")),
    ("行动", ("行动建议", "今日行动", "行动")),
)


class Invalid(Exception):
    """输入不合规。"""


def fail(code: int, msg: str) -> None:
    print(f"错误：{msg}", file=sys.stderr)
    sys.exit(code)


def dedup(raw, limit=None):
    if not isinstance(raw, list):
        raise Invalid("tags/sources 必须是数组")
    seen, out = set(), []
    for x in raw:
        s = str(x).strip()
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    if limit and len(out) > limit:
        out = out[:limit]
    return out


def validate(data: dict) -> dict:
    if not isinstance(data, dict):
        raise Invalid("顶层必须是 JSON 对象")

    # Reject legacy short-brief schema without body_markdown
    if "body_markdown" not in data and data.get("sections"):
        raise Invalid(
            "检测到旧版短讯 schema（sections/items）。"
            "本仓库已统一为深读标准：请提供 body_markdown。"
            "详见 docs/BOT.md"
        )

    raw_date = data.get("date") or datetime.now(TZ).date().isoformat()
    if not DATE_RE.match(str(raw_date)):
        raise Invalid(f"date 必须是 YYYY-MM-DD，收到 {raw_date!r}")
    try:
        d = date.fromisoformat(str(raw_date))
    except ValueError as e:
        raise Invalid(f"date 不是合法日期：{raw_date!r}") from e

    today = datetime.now(TZ).date()
    if d > today + timedelta(days=1):
        raise Invalid(f"date {d} 在未来太远（今天是 {today}）")

    summary = str(data.get("summary") or "").strip()
    if not summary:
        raise Invalid("summary 必填（首页卡片摘要）")

    body = str(data.get("body_markdown") or "").strip()
    if not body:
        raise Invalid("body_markdown 必填（深读正文 Markdown）")
    if body.lstrip().startswith("---"):
        raise Invalid("body_markdown 不要包含 YAML front matter；脚本会生成")

    compact = re.sub(r"\s+", "", body)
    if len(compact) < MIN_BODY_CHARS:
        raise Invalid(
            f"正文过短：去空白后 {len(compact)} 字符，下限 {MIN_BODY_CHARS}。"
            "请按 docs/BOT.md 深读结构写满主线解析。"
        )

    for label, keys in REQUIRED_SEMANTICS:
        if not any(k in body for k in keys):
            raise Invalid(
                f"正文缺少「{label}」相关标题（需包含其一：{', '.join(keys)}）"
            )

    title = str(data.get("title") or f"{d.isoformat()} AI 深读").strip()

    return {
        "date": d,
        "title": title,
        "summary": summary,
        "tags": dedup(data.get("tags") or [], MAX_TAGS),
        "sources": dedup(data.get("sources") or []),
        "body_markdown": body,
        "body_chars": len(compact),
    }


def render(b: dict) -> str:
    q = json.dumps
    fm = [
        "---",
        f"title: {q(b['title'], ensure_ascii=False)}",
        f"date: {b['date'].isoformat()}T08:00:00+08:00",
        f"summary: {q(b['summary'], ensure_ascii=False)}",
    ]
    if b["tags"]:
        fm.append(
            "tags: [" + ", ".join(q(t, ensure_ascii=False) for t in b["tags"]) + "]"
        )
    if b["sources"]:
        fm.append(
            "sources: ["
            + ", ".join(q(s, ensure_ascii=False) for s in b["sources"])
            + "]"
        )
    fm.append("---")
    return "\n".join(fm) + "\n\n" + b["body_markdown"].rstrip() + "\n"


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, **kw)


def hugo_build() -> bool:
    try:
        probe = run(["hugo", "version"])
    except FileNotFoundError:
        print("提示：没找到 hugo，跳过构建校验", file=sys.stderr)
        return True
    if probe.returncode != 0:
        print("提示：没找到 hugo，跳过构建校验", file=sys.stderr)
        return True
    r = run(["hugo", "--minify", "--quiet"])
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
        return False
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description="生成并提交一篇每日 AI 深读报告")
    ap.add_argument("--json", type=Path, help="读取 JSON 文件（默认 stdin）")
    ap.add_argument("--check", action="store_true", help="只校验并打印，不写文件")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的当天报告")
    ap.add_argument("--commit", action="store_true", help="写入后 git commit")
    ap.add_argument("--push", action="store_true", help="commit 后 push origin main")
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
            f"--- 校验通过：深读 {brief['body_chars']} 字符 → {path.relative_to(REPO)}",
            file=sys.stderr,
        )
        return

    existed = path.exists()
    if existed and not args.force:
        fail(2, f"{path.relative_to(REPO)} 已存在。确认覆盖加 --force")

    backup = path.read_text(encoding="utf-8") if existed else None
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"已写入 {path.relative_to(REPO)}（深读 {brief['body_chars']} 字符）")

    try:
        ok = hugo_build()
    except FileNotFoundError:
        print("提示：没找到 hugo，跳过构建校验", file=sys.stderr)
        ok = True
    if not ok:
        if backup is None:
            path.unlink()
        else:
            path.write_text(backup, encoding="utf-8")
        fail(3, "Hugo 构建失败，已回滚")

    if not (args.commit or args.push):
        return

    msg = f"content: {brief['date'].isoformat()} AI 深读"
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
