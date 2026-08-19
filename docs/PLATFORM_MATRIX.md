# Platform Matrix

CRIT Universal is LLM-agnostic. Platform adapters change **where the instructions live**, not the semantic protocol.

| Platform | Recommended adapter | Persistent location | Notes |
|---|---|---|---|
| Claude Code | `SKILL.md` + router | `~/.claude/skills/...` + `~/.claude/CLAUDE.md` or repository scope | Skill can be invoked directly or auto-routed by instructions |
| Claude Project | Project instructions | Project instructions | Same v1.1 semantic core |
| ChatGPT Project | Project instructions | Project settings -> Project instructions | Same v1.1 semantic core |
| Gemini App | Gem instructions | Custom Gem -> Instructions | Same v1.1 semantic core |
| Gemini CLI | `GEMINI.md` | Project root or `~/.gemini/GEMINI.md` | Same v1.1 semantic core |
| GitHub Copilot | Repository instructions | `.github/copilot-instructions.md` | Repository evidence/test rules remain authoritative |
| AGENTS.md-compatible agent | `AGENTS.md` | Project or workspace scope | Use `adapters/agents-md/AGENTS.md` |
| Local/open model UI | Generic system instructions | System/custom instruction field | Use `adapters/generic/SYSTEM_INSTRUCTIONS.md` |
| Unlisted LLM | Generic system instructions | Any persistent instruction mechanism | See `docs/LLM_AGNOSTIC.md` |

## Universal fallback

If a product is not listed, use:

```text
adapters/generic/SYSTEM_INSTRUCTIONS.md
```

If the product has no persistent instruction feature, provide that instruction block at the beginning of the problem-solving conversation.

## Important distinction

Adapters do not make model behavior programmatically deterministic. They make the semantic contract portable and testable.

Behavioral reliability must be measured against `tests/behavioral/` for the specific model/version being used. Package conformance alone is not model-performance proof.
