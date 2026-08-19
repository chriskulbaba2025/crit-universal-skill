<p align="center">
  <img src="branding/logo.svg" alt="CRIT Universal" width="760">
</p>

<p align="center">
  <strong>Context before command. Robustness before confidence.</strong><br>
  An LLM-agnostic problem-solving protocol that makes AI understand the problem, test the assumption most capable of changing the answer, and match certainty to the consequences of being wrong.
</p>

<p align="center">
  <code>v1.1.0</code> · <strong>99/100 package conformance</strong> · Claude · ChatGPT · Gemini · Copilot · local models · generic LLMs
</p>

> **Independent, unofficial implementation.** CRIT™ is used descriptively for the Context-Role-Interview-Task framework demonstrated publicly by Geoff Woods. This repository is not affiliated with or endorsed by Geoff Woods, AI Leadership, or *The AI-Driven Leader*. The implementation, adapters, robustness controls, validation system, and documentation are independently authored.

---

# CRIT Universal

**CRIT Universal is an LLM-agnostic reasoning protocol.** It can be used with Claude, ChatGPT, Gemini, Copilot, local/open models, coding agents, or any other model that accepts persistent or per-session instructions.

The source CRIT method establishes **Context -> Role -> Interview -> Task**. CRIT Universal preserves that discovery order, then adds the controls needed for repeated real-world decisions: a Decision Contract, a Robustness Gate, revision preservation, top-down decomposition, hard verification gates, and behavioral conformance fixtures.

## What changed in v1.1

The core question is no longer merely:

> Have we challenged the assumptions?

It is:

> **Would this recommendation still hold if the uncertain premise most capable of changing it were wrong?**

For substantial work CRIT now evaluates:

```text
objective
+ decision owner
+ success condition
+ cost of error
+ reversibility
+ evidence sufficiency
+ highest-leverage uncertain assumption
+ strongest credible disconfirming condition
```

Then it uses one of three internal states:

- **PROCEED** - robust enough for the decision exposure;
- **CONDITIONAL** - useful, but materially assumption-sensitive;
- **BLOCKED** - stronger evidence is required before responsible confidence.

## Operating cycle

```text
ROUTE
  ↓
CONTEXT
  ↓
ROLE
  ↓
INTERVIEW (0-3 decision-changing questions)
  ↓
DECISION CONTRACT
  ↓
ROBUSTNESS GATE
  ↓
TASK
  ↓
PRODUCE
  ↓
CRITIQUE
  ↓
PRESERVE / DEEPEN
  ↓
VERIFY (hard PASS/FAIL gates)
  ↓
DELIVER
```

## Why this is more predictable

CRIT v1.1 constrains the judgment points that most often cause LLM drift:

- interview questions must pass a counterfactual value test;
- the three-question cap cannot be mistaken for evidence sufficiency;
- role cannot predetermine conclusion;
- preferences cannot silently become facts;
- evidence is evaluated relative to the claim;
- only the highest-leverage uncertain assumption is robustness-tested;
- verification depth scales with downside and reversibility;
- approval locks do not freeze contradicted assumptions;
- runtime numeric self-grading is removed.

## LLM-agnostic quick start

### Any LLM

Use:

```text
adapters/generic/SYSTEM_INSTRUCTIONS.md
```

as the platform's system prompt, custom instructions, workspace/project instructions, agent rule, persistent context, or reusable prompt preset.

If your agent supports `AGENTS.md`, use:

```text
adapters/agents-md/AGENTS.md
```

Full model-neutral instructions: [`docs/LLM_AGNOSTIC.md`](docs/LLM_AGNOSTIC.md)

### Claude Code

Copy `.claude/skills/crit-problem-solving/SKILL.md` to your personal or project skills directory, then use `GLOBAL_CLAUDE_RULE.md` for automatic routing.

### ChatGPT Project

Paste `adapters/chatgpt-project/PROJECT_INSTRUCTIONS.md` into Project instructions.

### Claude Project

Paste `adapters/claude-project/PROJECT_INSTRUCTIONS.md` into project instructions.

### Gemini

Use the Gem or Gemini CLI adapter in `adapters/`.

### GitHub Copilot

Copy `adapters/github-copilot/copilot-instructions.md` to `.github/copilot-instructions.md`.

See [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Canonical Agent Skills-compatible skill |
| [`core/CRIT_CORE.md`](core/CRIT_CORE.md) | Platform-neutral semantic specification |
| [`core/ROUTER.md`](core/ROUTER.md) | CRIT vs DIRECT routing |
| [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) | Global Claude Code auto-routing rule |
| [`adapters/`](adapters/) | Model/platform loading adapters |
| [`docs/LLM_AGNOSTIC.md`](docs/LLM_AGNOSTIC.md) | Use CRIT with any LLM |
| [`docs/INSTALLATION.md`](docs/INSTALLATION.md) | Platform installation |
| [`docs/METHOD.md`](docs/METHOD.md) | Method and v1.1 rationale |
| [`tests/behavioral/`](tests/behavioral/) | Provider-neutral behavioral conformance fixtures |
| [`scripts/validate-package.py`](scripts/validate-package.py) | Package/invariant validator |
| [`scripts/validate-behavioral-fixtures.py`](scripts/validate-behavioral-fixtures.py) | Behavioral fixture schema validator |
| [`SCORECARD.md`](SCORECARD.md) | Package conformance scorecard |
| [`REPOSITORY_METADATA.md`](REPOSITORY_METADATA.md) | Canonical GitHub About description and suggested topics |
| [`branding/`](branding/) | Logo, icon, social-card assets |

## Evidence discipline

CRIT does not use a rigid source hierarchy. Evidence is evaluated relative to a claim using:

- relevance;
- reliability;
- directness;
- recency;
- independence.

Direct test or execution evidence remains decisive where the task can actually be tested.

## Verification

Runtime self-scoring has been removed.

Substantial outputs must pass hard gates for:

```text
Problem fidelity
Hard constraints
Anti-goals
Material assumptions treated
Evidence discipline
Authority boundary
Actionability / usable outcome
Robustness state represented honestly
```

If evidence cannot support a normal release, the answer must remain conditional or blocked rather than manufacture certainty.

## Behavioral conformance

The repository's **99/100** is a package conformance score. It does not claim 99% reasoning reliability.

`tests/behavioral/cases.json` defines adversarial cases for routing, question efficiency, premise challenge, reversibility, evidence sufficiency, preservation, and hard constraints. The same cases can be run against different model families without requiring identical wording.

## Validation

Run:

```bash
python scripts/validate-package.py
python scripts/validate-behavioral-fixtures.py
```

CI runs both validators.

## Status

**Version:** 1.1.0  
**Release state:** Stable candidate pending branch validation/merge  
**Canonical maintainer:** Chris Kulbaba (@chriskulbaba2025)  
**Canonical repository:** `chriskulbaba2025/crit-universal-skill`

## License and attribution

The original implementation and repository content are MIT licensed. Third-party names and marks are not granted by that license. See [`LICENSE`](LICENSE), [`NOTICE.md`](NOTICE.md), and [`SOURCES.md`](SOURCES.md).
