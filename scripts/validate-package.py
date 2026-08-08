#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"

required = [
    "README.md", "SKILL.md", "GLOBAL_CLAUDE_RULE.md", "LICENSE", "NOTICE.md",
    "SOURCES.md", "SCORECARD.md", "core/CRIT_CORE.md", "core/ROUTER.md",
    ".claude/skills/crit-problem-solving/SKILL.md",
    "adapters/chatgpt-project/PROJECT_INSTRUCTIONS.md",
    "adapters/claude-project/PROJECT_INSTRUCTIONS.md",
    "adapters/claude-code/CLAUDE_RULE.md",
    "adapters/gemini-gem/GEM_INSTRUCTIONS.md",
    "adapters/gemini-cli/GEMINI.md",
    "adapters/generic/SYSTEM_INSTRUCTIONS.md",
    "adapters/agents-md/AGENTS.md",
    "adapters/github-copilot/copilot-instructions.md",
    "docs/INSTALLATION.md", "docs/METHOD.md", "docs/PLATFORM_MATRIX.md",
    "branding/logo.svg", "branding/icon.svg", "branding/social-card.svg",
]

errors = []

for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

root_skill = ROOT / "SKILL.md"
claude_skill = ROOT / ".claude/skills/crit-problem-solving/SKILL.md"
if root_skill.is_file() and claude_skill.is_file():
    if root_skill.read_bytes() != claude_skill.read_bytes():
        errors.append("Claude Code distribution SKILL.md differs from root SKILL.md")

core = (ROOT / "core/CRIT_CORE.md").read_text(encoding="utf-8") if (ROOT / "core/CRIT_CORE.md").exists() else ""
core_required = [
    "Context - construct the problem environment",
    "Role - define perspective and relationship",
    "Interview - resolve the highest-value uncertainty",
    "one question at a time",
    "no more than three questions",
    "Anti-goals",
    "Preserve and deepen",
    "Five-area semantic audit",
    "Total >= 95 / 100",
]
for phrase in core_required:
    if phrase.lower() not in core.lower():
        errors.append(f"core invariant missing: {phrase}")

adapter_paths = [
    "adapters/chatgpt-project/PROJECT_INSTRUCTIONS.md",
    "adapters/claude-project/PROJECT_INSTRUCTIONS.md",
    "adapters/claude-code/CLAUDE_RULE.md",
    "adapters/gemini-gem/GEM_INSTRUCTIONS.md",
    "adapters/gemini-cli/GEMINI.md",
    "adapters/generic/SYSTEM_INSTRUCTIONS.md",
    "adapters/agents-md/AGENTS.md",
    "adapters/github-copilot/copilot-instructions.md",
]
for rel in adapter_paths:
    p = ROOT / rel
    if p.exists():
        text = p.read_text(encoding="utf-8")
        if f"CRIT_CORE_VERSION: {VERSION}" not in text:
            errors.append(f"adapter missing core version marker: {rel}")
        for semantic in ["Context", "Role", "Interview", "Task", "95"]:
            if semantic.lower() not in text.lower():
                errors.append(f"adapter missing semantic token {semantic!r}: {rel}")

# Check local markdown links that point to repository files.
md_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for p in ROOT.rglob("*.md"):
    text = p.read_text(encoding="utf-8")
    for target in md_link.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (p.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"link escapes repository: {p.relative_to(ROOT)} -> {target}")
            continue
        if not resolved.exists():
            errors.append(f"broken relative link: {p.relative_to(ROOT)} -> {target}")

# Public package hygiene: internal study artifacts must never ship.
for p in ROOT.rglob("*"):
    if not p.is_file():
        continue
    name = p.name.lower()
    if "strategic_analysis" in name or "strategic-analysis" in name or name.endswith(".mp3"):
        errors.append(f"internal/source artifact must not ship: {p.relative_to(ROOT)}")

# Basic frontmatter check.
skill = root_skill.read_text(encoding="utf-8") if root_skill.exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing YAML frontmatter")
if "name: crit-problem-solving" not in skill:
    errors.append("SKILL.md has wrong or missing name")
if "description:" not in skill:
    errors.append("SKILL.md missing description")

if errors:
    print("CRIT Universal package validation: FAIL")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("CRIT Universal package validation: PASS")
print(f"- required files: {len(required)}")
print(f"- adapters version-aligned: {len(adapter_paths)}")
print("- root/Claude skill parity: PASS")
print("- core semantic invariants: PASS")
print("- relative Markdown links: PASS")
print("- public-package hygiene: PASS")
