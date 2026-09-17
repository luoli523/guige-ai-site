#!/usr/bin/env python3
"""新内容发布后，用 Resend Broadcasts 给对应名单发一封「摘要 + 链接」邮件。

用法：
    RESEND_API_KEY=... python3 scripts/notify_subscribers.py \
        --kind daily --file content/daily/2026-09-15.md \
        --base-url https://luoli523.github.io/guige-ai-site \
        --audience <Resend audience id> [--dry-run]

    --kind daily : 本站每日简报，正文 = summary + 一分钟速览 + 执行摘要 + 链接
    --kind post  : 主站博客文章，正文 = description + 链接
    --kind poem  : 鬼话诗，正文 = 诗句 + summary（引子）+ 链接
    --dry-run    : 只在 Resend 建草稿 broadcast，不发送

主站与诗词站的 workflow 直接拉取本文件使用，改接口时三处一起看。
名单、发件人等配置见 guige-subscribe 仓库 README。

退出码：0 已发送 / 已存在跳过 / 未配置 key（不阻塞部署）；1 参数或 API 错误。
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.resend.com"
FROM = "鬼哥 <hi@guige.ai>"
REPLY_TO = "luoli523@gmail.com"
FOOTER = "你收到这封邮件是因为在鬼哥的站点订阅了更新。不想再收：{{{RESEND_UNSUBSCRIBE_URL}}}"


def parse_front_matter(text: str) -> tuple[dict, str]:
    """只解析 `key: value` 一层的 YAML，够三个站的 front matter 用。"""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise SystemExit("错误：文件没有 YAML front matter")
    meta = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if km:
            v = km.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            meta[km.group(1)] = v
    return meta, m.group(2)


def section(body: str, heading: str) -> str:
    """取某个 `## 标题` 下、到下一个 `##` 之前的正文。"""
    m = re.search(rf"^##[^#\n]*{re.escape(heading)}[^\n]*\n(.*?)(?=^##[^#]|\Z)", body, re.M | re.S)
    return m.group(1).strip() if m else ""


# --- 极简 Markdown → HTML：只覆盖简报里会出现的标题、列表、段落、加粗、链接 ---

def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def md_to_html(md: str) -> str:
    out, para, items = [], [], []

    def flush():
        nonlocal para, items
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items = []

    for line in md.splitlines():
        s = line.strip()
        if not s:
            flush()
        elif s.startswith("#"):
            flush()
            out.append(f"<h3>{inline(s.lstrip('#').strip())}</h3>")
        elif re.match(r"^[-*]\s+", s):
            if para:
                flush()
            items.append(re.sub(r"^[-*]\s+", "", s))
        elif s.startswith(">"):
            flush()
            out.append(f"<blockquote>{inline(s.lstrip('>').strip())}</blockquote>")
        else:
            if items:
                flush()
            para.append(s)
    flush()
    return "\n".join(out)


def wrap(title: str, body_html: str, url: str) -> str:
    return f"""<div style="font:16px/1.75 -apple-system,'Noto Serif SC','Source Han Serif SC',serif;color:#1e2230;max-width:38em;margin:0 auto;padding:24px">
<h2 style="font-size:1.35rem;margin:0 0 16px">{html.escape(title)}</h2>
{body_html}
<p style="margin:28px 0"><a href="{html.escape(url)}" style="background:#2dd4bf;color:#07090f;padding:12px 22px;border-radius:8px;text-decoration:none;font-weight:600">阅读全文 →</a></p>
<p style="color:#6a6f7d;font-size:13px;border-top:1px solid #e5e5e5;padding-top:14px">{FOOTER}</p>
</div>"""


# --- 三种内容 ---

def build_daily(meta: dict, body: str, base: str, path: Path) -> tuple[str, str, str, str]:
    url = f"{base}/daily/{path.stem}/"
    title = meta.get("title") or path.stem
    md = []
    if meta.get("summary"):
        md.append(f"> {meta['summary']}")
    if g := section(body, "一分钟速览"):
        md.append("## 一分钟速览\n\n" + g)
    if d := section(body, "执行摘要"):
        md.append("## 执行摘要\n\n" + d)
    md.append("本期由自动化流水线采集与生成，未经逐条人工核实，请以原始信源为准。")
    text = "\n\n".join(md) + f"\n\n阅读全文：{url}\n\n{FOOTER}"
    return title, wrap(title, md_to_html("\n\n".join(md)), url), text, url


def build_post(meta: dict, body: str, base: str, path: Path) -> tuple[str, str, str, str]:
    slug = meta.get("slug") or path.parent.name
    url = f"{base}/p/{slug}/"
    title = meta.get("title") or slug
    desc = meta.get("description") or meta.get("summary") or ""
    text = (desc + "\n\n" if desc else "") + f"阅读全文：{url}\n\n{FOOTER}"
    return title, wrap(title, md_to_html(desc), url), text, url


def build_poem(meta: dict, body: str, base: str, path: Path) -> tuple[str, str, str, str]:
    url = f"{base}/poems/{urllib.parse.quote(path.parent.name)}/"
    title = meta.get("title") or path.parent.name
    who = "·".join(x for x in (meta.get("dynasty"), meta.get("author")) if x)
    lines = [l.strip() for l in section(body, "诗词全文").splitlines() if l.strip()]
    poem_html = "<p style=\"font-size:1.25rem;line-height:2\">" + "<br>".join(html.escape(l) for l in lines) + "</p>"
    parts_html = (f"<p style=\"color:#6a6f7d\">{html.escape(who)}</p>" if who else "") + poem_html
    if meta.get("summary"):
        parts_html += f"<p>{html.escape(meta['summary'])}</p>"
    subject = f"{title}" + (f" · {who}" if who else "")
    text = (who + "\n\n" if who else "") + "\n".join(lines) + "\n\n" + meta.get("summary", "") + f"\n\n读这首的背后：{url}\n\n{FOOTER}"
    return subject, wrap(title, parts_html, url), text, url


BUILDERS = {"daily": build_daily, "post": build_post, "poem": build_poem}


# --- Resend ---

def api(method: str, endpoint: str, key: str, payload: dict | None = None) -> dict:
    req = urllib.request.Request(
        f"{API}/{endpoint}", method=method,
        data=json.dumps(payload).encode() if payload is not None else None,
        # Resend 前面的 Cloudflare 会拦默认的 Python-urllib UA（1010），所以显式给一个
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "User-Agent": "guige-notify/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"错误：Resend API {method} {endpoint} → {e.code} {e.read().decode()[:400]}")


def ident(kind: str, path: Path) -> str:
    """broadcast 的 name，作幂等键；Resend 限 70 字符，超长时截断并缀短哈希。"""
    key = f"{kind}/{path.stem if kind == 'daily' else path.parent.name}"
    if len(key) > 70:
        key = key[:60] + "~" + hashlib.sha1(key.encode()).hexdigest()[:8]
    return key


def already_sent(key: str, name: str) -> bool:
    data = api("GET", "broadcasts?limit=100", key)
    return any(b.get("name") == name for b in data.get("data", []))


def main() -> None:
    ap = argparse.ArgumentParser(description="发布后通知邮件订阅者（Resend Broadcasts）")
    ap.add_argument("--kind", choices=sorted(BUILDERS), required=True)
    ap.add_argument("--file", type=Path, required=True)
    ap.add_argument("--base-url", required=True, help="站点根地址，不带末尾斜杠")
    ap.add_argument("--audience", required=True, help="Resend audience（segment）id")
    ap.add_argument("--dry-run", action="store_true", help="只建草稿不发送")
    args = ap.parse_args()

    key = os.environ.get("RESEND_API_KEY", "").strip()
    if not key:
        print("未设置 RESEND_API_KEY，跳过订阅者通知")
        return

    meta, body = parse_front_matter(args.file.read_text(encoding="utf-8"))
    subject, html_body, text, url = BUILDERS[args.kind](meta, body, args.base_url.rstrip("/"), args.file)

    name = ident(args.kind, args.file)
    if already_sent(key, name):
        print(f"已存在 broadcast「{name}」（{url}），跳过")
        return

    resp = api("POST", "broadcasts", key, {
        "segment_id": args.audience,
        "from": FROM,
        "reply_to": REPLY_TO,
        "subject": subject,
        "html": html_body,
        "text": text,
        "name": name,
        "send": not args.dry_run,
    })
    print(f"{'已建草稿' if args.dry_run else '已发送'}：{subject} → broadcast {resp.get('id')}")


if __name__ == "__main__":
    main()
