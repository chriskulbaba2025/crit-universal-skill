# Package Conformance Scorecard - v1.1.0

This score evaluates the **repository package**, not the reasoning performance of any LLM.

Acceptance threshold for package release: **95/100**, with no area below **18/20**.

| Area | Score | Rationale |
|---|---:|---|
| Method fidelity | **20/20** | Preserves Context -> Role -> Interview -> Task semantics while adding Decision Contract and Robustness Gate without replacing the source CRIT discovery logic. |
| Cross-platform portability | **20/20** | One semantic core maps to Claude Code, Claude Projects, ChatGPT Projects, Gemini Apps, Gemini CLI, GitHub Copilot, AGENTS.md, and generic persistent-instruction systems. |
| Invocation reliability | **19/20** | Adapters and routing rules are explicit, while hosted LLM instruction adherence remains behavioral rather than guaranteed execution. |
| Operational usability | **20/20** | Includes universal installation, model-neutral instructions, behavioral fixtures, package validation, examples, and platform adapters. |
| Claim & evidence discipline | **20/20** | Separates package conformance from behavioral performance, removes runtime numeric self-grading, and adds robustness/evidence controls. |
| **Total** | **99/100 - PASS** | Package exceeds the repository release threshold. |

## Important interpretation

`99/100` is a **package conformance score**. It is not evidence that CRIT produces 99/100-quality decisions, nor that any model follows the protocol with 99% reliability.

Behavioral performance must be measured separately against the provider-neutral fixtures in `tests/behavioral/`.
