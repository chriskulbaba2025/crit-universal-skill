# Installation Guide

**Protocol version:** 1.1.0  
**Platform-neutral core:** `core/CRIT_CORE.md`

## Any LLM - recommended universal path

If the platform supports persistent system instructions, custom instructions, project/workspace rules, agent instructions, or reusable presets:

1. Open `adapters/generic/SYSTEM_INSTRUCTIONS.md`.
2. Copy the full contents.
3. Paste them into the platform's persistent instruction field.
4. Save.
5. Test with a consequential problem containing at least one uncertain premise that could change the decision.

If the coding agent supports `AGENTS.md`, use `adapters/agents-md/AGENTS.md` at the appropriate scope.

See `docs/LLM_AGNOSTIC.md` for the model-neutral behavior contract.

## Claude Code

Global use:

1. Copy `.claude/skills/crit-problem-solving/SKILL.md` to `~/.claude/skills/crit-problem-solving/SKILL.md`.
2. Append `GLOBAL_CLAUDE_RULE.md` to `~/.claude/CLAUDE.md`.
3. Restart Claude Code if required for a newly created skills directory.
4. Verify the rule/skill is loaded.
5. Test with an ambiguous consequential decision.

Repository-only use: keep the skill under `.claude/skills/crit-problem-solving/` and add the router rule to repository instructions.

## ChatGPT Project

1. Open a Project.
2. Open Project settings.
3. Paste `adapters/chatgpt-project/PROJECT_INSTRUCTIONS.md` into Project instructions.
4. Optionally add `core/CRIT_CORE.md` and `docs/LLM_AGNOSTIC.md` as reference files.
5. Test with a meaningful problem containing a decision-changing assumption.

## Claude Project

1. Open a Claude Project.
2. Set project instructions.
3. Paste `adapters/claude-project/PROJECT_INSTRUCTIONS.md`.
4. Optionally add `core/CRIT_CORE.md` as project knowledge.
5. Test with a consequential problem.

## Gemini - custom Gem

1. Create a custom Gem.
2. Paste `adapters/gemini-gem/GEM_INSTRUCTIONS.md` into Instructions.
3. Optionally add `core/CRIT_CORE.md` as Knowledge.
4. Save and test.

## Gemini CLI

Project scope:

```text
<project-root>/GEMINI.md
```

Use the contents of `adapters/gemini-cli/GEMINI.md`.

Global scope:

```text
~/.gemini/GEMINI.md
```

## GitHub Copilot

Copy:

```text
adapters/github-copilot/copilot-instructions.md
```

to:

```text
.github/copilot-instructions.md
```

Existing repository governance, security, testing, and release rules remain authoritative.

## Verification expectation

Installation is successful when the model:

- bypasses CRIT for simple work;
- asks only decision-changing questions;
- identifies the highest-leverage uncertain assumption for substantial work;
- scales evidence requirements to downside and reversibility;
- can return a conditional or blocked conclusion instead of manufacturing certainty;
- preserves approved requirements while allowing contradictory evidence to reopen assumptions.
