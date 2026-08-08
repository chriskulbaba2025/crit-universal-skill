# Claude Code adapter

Recommended installation has two layers:

1. Install the skill at `~/.claude/skills/crit-problem-solving/SKILL.md` for personal/global use, or `.claude/skills/crit-problem-solving/SKILL.md` inside a repository for project-only use.
2. Add `GLOBAL_CLAUDE_RULE.md` to `~/.claude/CLAUDE.md` so every prompt is routed through the CRIT applicability check.

Claude Code can automatically load a skill when its description matches the request, and the skill can also be invoked directly as `/crit-problem-solving`.

Verify installation with `/memory` for CLAUDE.md instructions and by asking Claude Code to list or invoke `/crit-problem-solving`.

Official references:
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/memory
