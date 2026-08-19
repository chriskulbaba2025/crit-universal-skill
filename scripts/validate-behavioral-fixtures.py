#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "tests" / "behavioral" / "cases.json"
errors = []

try:
    cases = json.loads(path.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"Behavioral fixture validation: FAIL\n- cannot parse {path}: {exc}")
    sys.exit(1)

if not isinstance(cases, list) or not cases:
    errors.append("cases.json must contain a non-empty list")

required = {"id", "prompt", "expected_route", "expected_state", "must_identify", "must_not", "max_questions"}
ids = set()

for i, case in enumerate(cases):
    label = case.get("id", f"index-{i}") if isinstance(case, dict) else f"index-{i}"
    if not isinstance(case, dict):
        errors.append(f"{label}: case must be an object")
        continue
    missing = required - set(case)
    if missing:
        errors.append(f"{label}: missing fields {sorted(missing)}")
    cid = case.get("id")
    if not isinstance(cid, str) or not cid.strip():
        errors.append(f"{label}: id must be a non-empty string")
    elif cid in ids:
        errors.append(f"{label}: duplicate id")
    else:
        ids.add(cid)
    if case.get("expected_route") not in {"DIRECT", "CRIT_REQUIRED"}:
        errors.append(f"{label}: invalid expected_route")
    if not isinstance(case.get("max_questions"), int) or not 0 <= case.get("max_questions", -1) <= 3:
        errors.append(f"{label}: max_questions must be 0..3")
    for field in ("must_identify", "must_not"):
        if not isinstance(case.get(field), list):
            errors.append(f"{label}: {field} must be a list")

if errors:
    print("Behavioral fixture validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Behavioral fixture validation: PASS")
print(f"- cases: {len(cases)}")
print("- schema: PASS")
print("- unique ids: PASS")
