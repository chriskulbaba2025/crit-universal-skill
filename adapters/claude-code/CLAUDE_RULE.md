<!-- CRIT_CORE_VERSION: 1.1.0 -->
# CRIT Universal Router - Claude Code

For significant or ambiguous work where missing context or uncertainty could materially change the result, invoke `crit-problem-solving` before substantive implementation.

Sequence: **Context -> Role -> Interview -> Decision Contract -> Robustness Gate -> Task -> Produce -> Critique -> Preserve/Deepen -> Verify**.

Inspect repository evidence first. Ask zero to three decision-changing questions, one at a time. For substantial work, evaluate cost of error, reversibility, evidence sufficiency, the highest-leverage uncertain assumption, and the strongest credible disconfirming condition. Use `PROCEED`, `CONDITIONAL`, or `BLOCKED` internally.

Preserve approved requirements and unaffected behavior, but allow new contradictory evidence or test results to reopen dependent assumptions. Verify hard requirements and test evidence before delivery. Do not use runtime numeric self-scoring.

Skip full CRIT for simple lookups or fully specified low-ambiguity actions. Existing repository governance, security, authorization, testing, and release rules remain authoritative.
