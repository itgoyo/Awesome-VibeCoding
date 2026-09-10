#!/usr/bin/env python3
"""
Awesome Vibe Coding —— 数据采集脚本

通过 GitHub Search API 采集 vibe coding 相关仓库，筛选 Star >= 100 的项目，
更新 data/repos.json 中已收录仓库的 Star 数、语言、更新时间等元数据。

用法：
    python3 scripts/collect.py                # 刷新已收录项目的元数据
    python3 scripts/collect.py --discover     # 额外搜索发现新项目候选（输出到 candidates.json）

说明：
    - 未认证的 GitHub API 限流为 search 10 次/分钟、core 60 次/小时。
      如需大规模采集，请设置环境变量 GITHUB_TOKEN。
    - 脚本不会自动新增项目到清单里，只会更新已有条目的数据；
      新增项目请通过 PR 提交，以保证清单质量。
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA_FILE = os.path.join(ROOT, "data", "repos.json")

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()

# 用于 --discover 的搜索关键词
DISCOVER_QUERIES = [
    "topic:vibe-coding",
    "topic:vibecoding",
    "topic:ai-coding",
    "topic:ai-agents",
    "topic:mcp",
    "vibe coding in:name,description,readme",
    "ai coding assistant in:name,description stars:>500",
    "ai app builder in:name,description stars:>300",
    "AI hardware in:name,description stars:>100",
    "esp32 ai in:name,description stars:>100",
]


def api(url, retries=4, wait=25):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-vibecoding-collector",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                return json.load(resp)
        except Exception as exc:  # noqa: BLE001
            msg = str(exc)
            if "403" in msg or "429" in msg:
                print(f"  限流，等待 {wait}s 后重试… ({attempt + 1}/{retries})")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"重试耗尽: {url}")


def repo_meta(full_name):
    """获取单个仓库的元数据。"""
    x = api(f"https://api.github.com/repos/{full_name}")
    return {
        "full_name": x["full_name"],
        "url": x["html_url"],
        "desc_en": (x.get("description") or "").strip(),
        "stars": x["stargazers_count"],
        "language": x.get("language"),
        "license": (x.get("license") or {}).get("spdx_id"),
        "homepage": x.get("homepage"),
        "pushed_at": (x.get("pushed_at") or "")[:10],
        "created_at": (x.get("created_at") or "")[:10],
    }


def refresh():
    """刷新 data/repos.json 中所有已收录项目的元数据。"""
    if not os.path.exists(DATA_FILE):
        print(f"找不到 {DATA_FILE}，请先创建清单。")
        return
    data = json.load(open(DATA_FILE, encoding="utf-8"))
    cats = data["categories"]
    names = [r["full_name"] for c in cats for r in c["repos"]]
    print(f"共 {len(names)} 个项目待刷新")

    meta = {}
    for i, fn in enumerate(names, 1):
        try:
            meta[fn.lower()] = repo_meta(fn)
            print(f"  [{i}/{len(names)}] {fn} -> {meta[fn.lower()]['stars']} ★")
        except Exception as exc:  # noqa: BLE001
            print(f"  [{i}/{len(names)}] {fn} 失败: {exc}")
        time.sleep(1.0)

    changed = 0
    total_stars = 0
    for c in cats:
        for r in c["repos"]:
            m = meta.get(r["full_name"].lower())
            if not m:
                continue
            for key in ("stars", "language", "license", "homepage", "pushed_at", "created_at", "desc_en", "url"):
                if m.get(key) != r.get(key):
                    changed += 1
                    r[key] = m.get(key)
            total_stars += r["stars"]
        c["repos"].sort(key=lambda x: -x["stars"])

    data["total_stars"] = total_stars
    data["generated_at"] = time.strftime("%Y-%m-%d")
    json.dump(data, open(DATA_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\n完成：更新了 {changed} 个字段，累计 Star {total_stars}")

    # 提示低于门槛的项目
    low = [r["full_name"] for c in cats for r in c["repos"] if r["stars"] < 100]
    if low:
        print("注意：以下项目已低于 100 star，建议从清单中移除：")
        for n in low:
            print("  -", n)


def discover():
    """搜索发现新项目候选，输出 candidates.json。"""
    found = {}
    for i, q in enumerate(DISCOVER_QUERIES, 1):
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
            {"q": q, "sort": "stars", "order": "desc", "per_page": 100}
        )
        try:
            d = api(url)
        except Exception as exc:  # noqa: BLE001
            print(f"[{i}/{len(DISCOVER_QUERIES)}] {q} 失败: {exc}")
            continue
        print(f"[{i}/{len(DISCOVER_QUERIES)}] {q} -> {d.get('total_count')} 个结果")
        for r in d.get("items", []):
            if r["stargazers_count"] < 100:
                continue
            found[r["full_name"]] = {
                "full_name": r["full_name"],
                "url": r["html_url"],
                "desc_en": (r.get("description") or "").strip(),
                "stars": r["stargazers_count"],
                "language": r.get("language"),
                "topics": r.get("topics", []),
            }
        time.sleep(10)

    known = set()
    if os.path.exists(DATA_FILE):
        data = json.load(open(DATA_FILE, encoding="utf-8"))
        known = {r["full_name"].lower() for c in data["categories"] for r in c["repos"]}
    new = {k: v for k, v in found.items() if k.lower() not in known}

    out = os.path.join(ROOT, "candidates.json")
    json.dump(sorted(new.values(), key=lambda x: -x["stars"]),
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\n发现 {len(found)} 个项目，其中 {len(new)} 个尚未收录，已写入 {out}")


if __name__ == "__main__":
    if "--discover" in sys.argv:
        discover()
    else:
        refresh()
