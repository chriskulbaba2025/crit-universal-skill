# Installation Guide

**Platform guidance last verified:** 2026-08-08.

## Claude Code

Claude Code supports reusable skills through `SKILL.md`. Project skills live under `.claude/skills/<skill-name>/SKILL.md`; personal skills live under `~/.claude/skills/<skill-name>/SKILL.md`. Claude may load a relevant skill automatically, and `/crit-problem-solving` invokes it directly.

For CRIT to be considered on every prompt across all repositories:

1. Create `~/.claude/skills/crit-problem-solving/`.
2. Copy this repository's `.claude/skills/crit-problem-solving/SKILL.md` into that directory.
3. Open `~/.claude/CLAUDE.md` (create it if needed).
4. Append the contents of `GLOBAL_CLAUDE_RULE.md`.
5. Start/restart Claude Code if the top-level skills directory did not exist when the session began.
6. Verify loaded instructions with `/memory`.
7. Test with: `I have a difficult decision with multiple stakeholders and competing constraints.` Claude should begin CRIT discovery rather than jump straight to a solution.

For one repository only, keep the skill at `.claude/skills/crit-problem-solving/SKILL.md` and add the router rule to that repository's `CLAUDE.md` or `.claude/CLAUDE.md`.

Official docs:
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/memory

## ChatGPT Project

ChatGPT Projects support project-specific instructions and project files. Project instructions apply inside that project and override global custom instructions.

1. Open or create a ChatGPT Project.
2. Open the project menu -> **Project settings**.
3. Paste `adapters/chatgpt-project/PROJECT_INSTRUCTIONS.md` into **Project instructions**.
4. Save.
5. Optionally add `core/CRIT_CORE.md` and relevant examples as project files for human reference.
6. Test with a meaningful ambiguous problem. The project should ask only material CRIT interview questions before solving.

Official docs:
- https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt

## Claude Project

Claude Projects support project instructions plus a project knowledge base.

1. Open or create a Claude Project.
2. Select **Set project instructions**.
3. Paste `adapters/claude-project/PROJECT_INSTRUCTIONS.md`.
4. Save.
5. Optionally add `core/CRIT_CORE.md` to project knowledge as a reference artifact.
6. Test with a consequential decision that has missing context.

Official docs:
- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects

## Gemini - custom Gem

Gemini Apps support custom Gems with persistent instructions and optional Knowledge files.

1. Open Gemini on the web.
2. Open **Gems** -> **New Gem**.
3. Name it `CRIT Universal`.
4. Paste `adapters/gemini-gem/GEM_INSTRUCTIONS.md` into **Instructions**.
5. Optionally add `core/CRIT_CORE.md` under **Knowledge**.
6. Preview, then click **Save**.

Official docs:
- https://support.google.com/gemini/answer/15146780
- https://support.google.com/gemini/answer/15235603

## Gemini CLI

Gemini CLI loads `GEMINI.md` context files automatically. A project-root `GEMINI.md` is project-specific; `~/.gemini/GEMINI.md` is global.

Project install:

```text
<project-root>/GEMINI.md
```

Copy the content from `adapters/gemini-cli/GEMINI.md`.

Global install:

```text
~/.gemini/GEMINI.md
```

Verify with `/memory show` inside Gemini CLI.

Official docs:
- https://geminicli.com/docs/cli/gemini-md/

## GitHub Copilot

GitHub Copilot supports repository-wide instructions from `.github/copilot-instructions.md`.

1. Create `.github/` in the target repository if it does not exist.
2. Copy `adapters/github-copilot/copilot-instructions.md` to `.github/copilot-instructions.md`.
3. Save/commit the file.
4. In supported Copilot surfaces, verify the instructions file appears in the response references.

Official docs:
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions

## Generic LLM

If the platform offers a persistent system prompt, custom instructions, agent instructions, workspace rules, or reusable prompt preset, paste `adapters/generic/SYSTEM_INSTRUCTIONS.md` there.

If the coding agent supports `AGENTS.md`, use `adapters/agents-md/AGENTS.md` at the appropriate project scope.

The semantic protocol is platform-neutral. What differs by product is only **how reliably and automatically the instructions are loaded**.
