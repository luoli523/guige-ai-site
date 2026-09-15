#!/usr/bin/env python3
"""新文章发布后，通过 Buttondown API 给订阅者发一封「摘要 + 链接」邮件。

用法：
    BUTTONDOWN_API_KEY=... python3 scripts/notify_subscribers.py \
        --kind daily --file content/daily/2026-09-15.md \
        --base-url https://luoli523.github.io/guige-ai-site [--dry-run]

    --kind daily : 本站每日简报，正文取「一分钟速览」+「执行摘要」
    --kind post  : 主站博客文章，正文取 front matter 的 description
    --dry-run    : 只在 Buttondown 建草稿，不发送

主站的 deploy workflow 直接拉取本文件使用，改接口时两边一起看。

退出码：0 已发送 / 已存在跳过 / 未配置 key（不阻塞部署）；1 参数或 API 错误。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.buttondown.com/v1"


def parse_front_matter(text: str) -> tuple[dict, str]:
    """只解析 `key: value` 一层的 YAML，够本站和主站的 front matter 用。"""
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


def build_daily(meta: dict, body: str, base: str, path: Path) -> tuple[str, str, str]:
    url = f"{base}/daily/{path.stem}/"
    title = meta.get("title") or path.stem
    parts = []
    if meta.get("summary"):
        parts.append(f"> {meta['summary']}")
    glance = section(body, "一分钟速览")
    if glance:
        parts.append("## 一分钟速览\n\n" + glance)
    digest = section(body, "执行摘要")
    if digest:
        parts.append("## 执行摘要\n\n" + digest)
    parts.append(f"**[阅读全文 →]({url})**\n\n---\n\n"
                 "本期由自动化流水线采集与生成，未经逐条人工核实，请以原始信源为准。")
    return title, "\n\n".join(parts), url


def build_post(meta: dict, body: str, base: str, path: Path) -> tuple[str, str, str]:
    slug = meta.get("slug") or path.parent.name
    url = f"{base}/p/{slug}/"
    title = meta.get("title") or slug
    desc = meta.get("description") or meta.get("summary") or ""
    md = (f"{desc}\n\n" if desc else "") + f"**[阅读全文 →]({url})**"
    return title, md, url


def api(method: str, endpoint: str, key: str, payload: dict | None = None) -> dict:
    req = urllib.request.Request(
        f"{API}/{endpoint}",
        method=method,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={"Authorization": f"Token {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"错误：Buttondown API {method} {endpoint} → {e.code} {e.read().decode()[:400]}")


def already_sent(key: str, url: str) -> bool:
    data = api("GET", "emails?page_size=100", key)
    return any(e.get("canonical_url") == url for e in data.get("results", []))


def main() -> None:
    ap = argparse.ArgumentParser(description="发布后通知邮件订阅者")
    ap.add_argument("--kind", choices=["daily", "post"], required=True)
    ap.add_argument("--file", type=Path, required=True)
    ap.add_argument("--base-url", required=True, help="站点根地址，不带末尾斜杠")
    ap.add_argument("--dry-run", action="store_true", help="只建草稿不发送")
    args = ap.parse_args()

    key = os.environ.get("BUTTONDOWN_API_KEY", "").strip()
    if not key:
        print("未设置 BUTTONDOWN_API_KEY，跳过订阅者通知")
        return

    meta, body = parse_front_matter(args.file.read_text(encoding="utf-8"))
    base = args.base_url.rstrip("/")
    build = build_daily if args.kind == "daily" else build_post
    subject, md, url = build(meta, body, base, args.file)

    if already_sent(key, url):
        print(f"已存在指向 {url} 的邮件，跳过")
        return

    resp = api("POST", "emails", key, {
        "subject": subject,
        "body": md,
        "canonical_url": url,
        "status": "draft" if args.dry_run else "about_to_send",
    })
    print(f"{'已建草稿' if args.dry_run else '已发送'}：{subject} → {resp.get('absolute_url', resp.get('id'))}")


if __name__ == "__main__":
    main()
