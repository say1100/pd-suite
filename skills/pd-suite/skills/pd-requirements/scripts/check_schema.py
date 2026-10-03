#!/usr/bin/env python3
"""校验 requirements.md 的 schema。用法: python check_schema.py <path>。
退出码:0=通过,1=不通过。机读输出前缀:REQ_SCHEMA_JSON:"""
import json, re, sys

def main():
    if len(sys.argv) < 2:
        print("REQ_SCHEMA_JSON:" + json.dumps({"ok": False, "errors": ["missing file argument"]}, ensure_ascii=False))
        return 1
    try:
        text = open(sys.argv[1], encoding="utf-8").read()
    except OSError as e:
        print("REQ_SCHEMA_JSON:" + json.dumps({"ok": False, "errors": [f"cannot read: {e}"]}, ensure_ascii=False))
        return 1
    errors = []
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and re.match(r"^\|\s*REQ-\d+\s*\|", s):
            rows.append([c.strip() for c in s.strip("|").split("|")])
    if not rows:
        errors.append("未找到任何 REQ- 条目行(表头须为 | ID | 用户 | 场景 | 痛点 | 优先级 | 验收口径 |)")
    for r in rows:
        rid = r[0]
        if len(r) < 6:
            errors.append(f"{rid}: 列数不足 6(实际 {len(r)})")
            continue
        for i, field in enumerate(["用户", "场景", "痛点", "优先级", "验收口径"], start=1):
            if not r[i]:
                errors.append(f"{rid}: {field} 为空")
        if len(r) > 5 and r[4] not in ("P0", "P1", "P2"):
            errors.append(f"{rid}: 优先级 {r[4]} 不在 P0/P1/P2")
    ok = not errors
    print("REQ_SCHEMA_JSON:" + json.dumps({"ok": ok, "rows": len(rows), "errors": errors[:20]}, ensure_ascii=False))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
