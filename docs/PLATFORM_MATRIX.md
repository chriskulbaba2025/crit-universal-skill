# Platform Matrix

| Platform | Recommended adapter | Persistent location | Auto-considered each turn? | Direct invocation |
|---|---|---|---|---|
| Claude Code | `SKILL.md` + router | `~/.claude/skills/...` + `~/.claude/CLAUDE.md` | Yes, behaviorally; skills also auto-discover by relevance | `/crit-problem-solving` |
| Claude Project | Project instructions | Project -> Set project instructions | Yes inside that project | Ask to use CRIT |
| ChatGPT Project | Project instructions | Project settings -> Project instructions | Yes inside that project | Ask to use CRIT |
| Gemini App | Gem instructions | Custom Gem -> Instructions | Yes when using that Gem | Open the Gem |
| Gemini CLI | `GEMINI.md` | Project root or `~/.gemini/GEMINI.md` | Yes when context file is loaded | Normal prompt |
| GitHub Copilot | repository instructions | `.github/copilot-instructions.md` | Yes on supported repo-aware surfaces | Normal prompt |
| Other agents | Generic / `AGENTS.md` | Product-specific persistent instructions | Product-dependent | Product-dependent |

## Important distinction

Hosted chat products treat these as behavioral instructions. They do not provide a hard programmatic guarantee that an LLM will perfectly execute the workflow on every qualifying prompt.

Claude Code offers stronger mechanics because it combines persistent `CLAUDE.md` instructions, discoverable Agent Skills, and optional hooks. Even there, semantic classification of whether a problem is "CRIT-worthy" is a judgment task, so the default repository uses a concise router plus a skill rather than pretending semantic routing is a deterministic shell rule.
