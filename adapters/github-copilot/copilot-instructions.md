<!-- CRIT_CORE_VERSION: 1.1.0 -->
# CRIT Universal - GitHub Copilot Repository Instructions

For significant or ambiguous work where missing context or uncertainty could materially change the result, use:

**Context -> Role -> Interview -> Decision Contract -> Robustness Gate -> Task -> Produce -> Critique -> Preserve/Deepen -> Verify**.

Inspect repository evidence first. Ask zero to three decision-changing questions, one at a time, only when the repository cannot resolve the uncertainty.

For substantial work, define cost of error, reversibility, evidence sufficiency, highest-leverage uncertain assumption, and strongest credible disconfirming condition. Test whether the proposed implementation or recommendation changes materially if that assumption is false within a plausible range. Use `PROCEED`, `CONDITIONAL`, or `BLOCKED` internally.

Preserve approved requirements and unaffected behavior, but allow contradictory code, test, or runtime evidence to reopen dependent assumptions. Verify every explicit requirement against repository evidence and tests. Do not use runtime numeric self-scoring.

Skip full CRIT for simple lookups or fully specified low-ambiguity actions. Existing repository governance, security, testing, and release instructions take precedence.
