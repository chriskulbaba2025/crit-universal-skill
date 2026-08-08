<p align="center">
  <img src="branding/logo.svg" alt="CRIT Universal" width="760">
</p>

<p align="center">
  <strong>Context before command.</strong><br>
  A portable problem-solving skill that makes AI understand the problem before it tries to solve it.
</p>

<p align="center">
  <code>v1.0.0</code> · <strong>99/100 semantic quality score</strong> · Claude Code · Claude Projects · ChatGPT Projects · Gemini · Copilot · Generic LLMs
</p>

> **Independent, unofficial implementation.** CRIT™ is used descriptively for the Context-Role-Interview-Task framework demonstrated publicly by Geoff Woods. This repository is not affiliated with or endorsed by Geoff Woods, AI Leadership, or *The AI-Driven Leader*. The implementation, adapters, validation system, and documentation in this repository are independently authored.

---

# CRIT Universal

**CRIT Universal** turns the CRIT™ method into a reusable, cross-LLM operating skill.

The central rule is simple:

> **Do not get better at telling AI what to do. Get better at making AI understand the problem before it does anything.**

The source method defines **Context -> Role -> Interview -> Task**. This repository preserves that order, then adds the operational controls required for repeated real-world use: critique, revision preservation, top-down decomposition, hard-constraint verification, and a semantic quality gate.

## Why this exists

Most AI failures on meaningful work start before the answer: the model is asked to solve a problem it does not yet understand.

CRIT Universal fixes that root cause by forcing a shared problem model first. For qualifying problems it:

1. builds Context, including constraints and anti-goals;
2. defines the model's Role and authority boundary;
3. Interviews the user with at most three high-value questions, one at a time;
4. compiles the exact Task only after enough context exists;
5. produces and critiques the solution;
6. preserves approved work during revisions;
7. decomposes from approved parent structures downward; and
8. verifies hard constraints and semantic quality before final delivery.

## What triggers it

Use CRIT for meaningful ambiguity: strategy, decisions, diagnosis, root-cause work, planning, prioritization, delegation, architecture, system design, tradeoffs, organizational problems, and high-impact goals.

It deliberately bypasses simple factual questions, arithmetic, direct rewrites/translations, syntax lookups, and fully specified low-ambiguity actions.

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Canonical Agent Skills-compatible skill |
| [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) | Global Claude Code auto-routing rule |
| [`core/CRIT_CORE.md`](core/CRIT_CORE.md) | Platform-neutral semantic specification |
| [`core/ROUTER.md`](core/ROUTER.md) | Applicability/trigger logic |
| [`.claude/skills/crit-problem-solving/`](.claude/skills/crit-problem-solving/) | Ready-to-copy Claude Code skill |
| [`adapters/`](adapters/) | ChatGPT, Claude, Gemini, Copilot, AGENTS.md, generic adapters |
| [`docs/INSTALLATION.md`](docs/INSTALLATION.md) | Step-by-step platform installation |
| [`docs/METHOD.md`](docs/METHOD.md) | Method reconstruction and operating model |
| [`docs/PLATFORM_MATRIX.md`](docs/PLATFORM_MATRIX.md) | Where each adapter lives and how it auto-loads |
| [`examples/`](examples/) | Worked usage examples |
| [`scripts/validate-package.py`](scripts/validate-package.py) | Zero-dependency package validator |
| [`SCORECARD.md`](SCORECARD.md) | Five-area release quality audit |
| [`branding/`](branding/) | Logo, icon, and social-card assets |
| [`PUBLISH_TO_GITHUB.ps1`](PUBLISH_TO_GITHUB.ps1) | One-command Windows publisher |

## Quick start

### Claude Code - global, recommended

Copy:

```text
.claude/skills/crit-problem-solving/SKILL.md
```

to:

```text
~/.claude/skills/crit-problem-solving/SKILL.md
```

Then append [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) to:

```text
~/.claude/CLAUDE.md
```

Claude Code can auto-load skills when the description matches and can invoke the skill directly with `/crit-problem-solving`.

### ChatGPT Project

Open the project -> **Project settings** -> paste [`adapters/chatgpt-project/PROJECT_INSTRUCTIONS.md`](adapters/chatgpt-project/PROJECT_INSTRUCTIONS.md) into **Project instructions**.

### Claude Project

Open the project -> **Set project instructions** -> paste [`adapters/claude-project/PROJECT_INSTRUCTIONS.md`](adapters/claude-project/PROJECT_INSTRUCTIONS.md).

### Gemini App

Create a custom **Gem** -> paste [`adapters/gemini-gem/GEM_INSTRUCTIONS.md`](adapters/gemini-gem/GEM_INSTRUCTIONS.md) into **Instructions** -> Save.

### Gemini CLI

Copy [`adapters/gemini-cli/GEMINI.md`](adapters/gemini-cli/GEMINI.md) to the project root as `GEMINI.md`. For all projects, place it at `~/.gemini/GEMINI.md`.

### GitHub Copilot

Copy [`adapters/github-copilot/copilot-instructions.md`](adapters/github-copilot/copilot-instructions.md) to `.github/copilot-instructions.md` in the target repository.

### Any other LLM

Use [`adapters/generic/SYSTEM_INSTRUCTIONS.md`](adapters/generic/SYSTEM_INSTRUCTIONS.md) as persistent system/custom instructions, or use [`adapters/agents-md/AGENTS.md`](adapters/agents-md/AGENTS.md) with agents that support `AGENTS.md`.

See the full [`Installation Guide`](docs/INSTALLATION.md).

## The operating cycle

```text
ROUTE
  ↓
CONTEXT
  ↓
ROLE
  ↓
INTERVIEW (0-3 questions, one at a time)
  ↓
TASK
  ↓
PRODUCE
  ↓
CRITIQUE
  ↓
PRESERVE / DEEPEN
  ↓
VERIFY
  ↓
DELIVER
```

## Quality gate

Substantial outputs are internally reviewed in five semantic areas:

| Area | Max |
|---|---:|
| Problem-model fidelity | 20 |
| Requirement & constraint coverage | 20 |
| Reasoning & solution coherence | 20 |
| Actionability & specificity | 20 |
| Claim discipline & verification | 20 |

**Release threshold:** >=95/100 total and no area below 18/20.

This is a self-review mechanism, not a substitute for factual evidence, tests, source verification, or human authorization.

## Design choices

The repository deliberately preserves several mechanics demonstrated in the source method:

- anti-goals belong in Context;
- the Interview is capped and sequential;
- the substantive Task comes after discovery;
- approved content is protected against revision regression;
- deeper work is generated top-down from an approved parent structure;
- explicit constraints get a separate compliance pass.

See [`docs/METHOD.md`](docs/METHOD.md) and [`SOURCES.md`](SOURCES.md).

## Validation

Run:

```bash
python scripts/validate-package.py
```

The validator checks required files, adapter version alignment, skill parity, core invariants, relative Markdown links, and accidental inclusion of internal source materials.

## Status

**Version:** 1.0.0  
**Release state:** Stable  
**Canonical maintainer:** Chris Kulbaba (@chriskulbaba2025)  
**Intended canonical repository:** `chriskulbaba2025/crit-universal-skill`

## License and attribution

The original implementation and repository content are MIT licensed. Third-party names and marks are not granted by that license. See [`LICENSE`](LICENSE), [`NOTICE.md`](NOTICE.md), and [`SOURCES.md`](SOURCES.md).
