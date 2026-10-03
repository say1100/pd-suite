#!/usr/bin/env python3
"""指标卡校验。用法: python check_metrics.py <eval-plan.md>。
检查:指标卡六字段齐全;定义/阈值无模糊词(效果/不错/显著/明显/大幅)。
退出码:0=过,1=不过。机读前缀:METRICS_JSON:"""
import json, re, sys
from pathlib import Path

VAGUE = ["效果", "不错", "显著", "明显", "大幅"]
FIELDS = ["指标", "定义", "公式", "数据来源", "基线", "阈值"]

def main():
    errs = []
    if len(sys.argv) < 2:
        print("METRICS_JSON:" + json.dumps({"ok": False, "errors": ["missing file"]}, ensure_ascii=False))
        return 1
    try:
        text = Path(sys.argv[1]).read_text(encoding="utf-8")
    except OSError as e:
        print("METRICS_JSON:" + json.dumps({"ok": False, "errors": [f"cannot read: {e}"]}, ensure_ascii=False))
        return 1
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and not re.search(r"指标\s*\||---", s) and re.match(r"^\|[^|]+\|", s):
            rows.append([c.strip() for c in s.strip("|").split("|")])
    if not rows:
        errs.append("未找到指标卡行(表头:| 指标 | 定义 | 公式 | 数据来源 | 基线 | 阈值 |)")
    for r in rows:
        name = r[0] if r else "?"
        if len(r) < 6:
            errs.append(f"{name}: 字段不足 6(实际 {len(r)})")
            continue
        for i, f in enumerate(FIELDS):
            if not r[i]:
                errs.append(f"{name}: {f} 为空")
        joined = " ".join(r[1:2] + r[5:])
        for w in VAGUE:
            if w in joined:
                errs.append(f"{name}: 出现模糊词「{w}」")
    ok = not errs
    print("METRICS_JSON:" + json.dumps({"ok": ok, "cards": len(rows), "errors": errs[:20]}, ensure_ascii=False))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
