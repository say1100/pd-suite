#!/usr/bin/env python3
"""demo 交付门禁校验。用法: python check_demo_gate.py <交付目录>。
要求:link-matrix.md 存在且含 mermaid 块;track-events.md 存在且 ≥1 事件行;
四态矩阵(在 link-matrix.md 内,表头含"空态")行数 ≥ 页面清单行数。
退出码:0=过,1=不过。机读前缀:DEMO_GATE_JSON:"""
import json, re, sys
from pathlib import Path

def count_rows(path, pattern):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return -1
    return len([l for l in text.splitlines() if re.search(pattern, l)])

def main():
    errs = []
    d = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    lm = d / "link-matrix.md"
    te = d / "track-events.md"
    if not lm.exists():
        errs.append("缺少 link-matrix.md(链路图/任务覆盖)")
    elif "```mermaid" not in lm.read_text(encoding="utf-8"):
        errs.append("link-matrix.md 内未找到 mermaid 链路图块")
    pages = count_rows(lm, r"^\|\s*(?!页面|:---|---)[^|]+\|[^|]+\|") if lm.exists() else 0
    states = count_rows(lm, r"^\|[^|]+\|[^|]*空态") if lm.exists() else 0
    if lm.exists() and pages > 0 and states < pages:
        errs.append(f"四态矩阵行数({states})少于页面数({pages})")
    if not te.exists():
        errs.append("缺少 track-events.md(埋点清单)——pd-eval 拒收无埋点交付")
    else:
        ev = count_rows(te, r"^\|\s*\w+_")
        if ev < 1:
            errs.append("track-events.md 内未找到事件行(命名应为 对象_动作)")
    ok = not errs
    print("DEMO_GATE_JSON:" + json.dumps({"ok": ok, "pages": pages, "errors": errs}, ensure_ascii=False))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
