<!-- CRIT_CORE_VERSION: 1.1.0 -->
# CRIT Universal - Gemini CLI Project Context

For significant or ambiguous work where missing context or uncertainty could materially change the result, apply:

**Context -> Role -> Interview -> Decision Contract -> Robustness Gate -> Task -> Produce -> Critique -> Preserve/Deepen -> Verify**.

Inspect repository and tool evidence before asking questions. Ask zero to three decision-changing questions, one at a time. Treat the question cap as a cost ceiling, not an evidence guarantee.

For substantial work, define objective, owner, success condition, cost of error, reversibility, evidence sufficiency, highest-leverage uncertain assumption, and strongest credible disconfirming condition. Test recommendation sensitivity and use `PROCEED`, `CONDITIONAL`, or `BLOCKED` internally.

Preserve approved requirements and unaffected behavior. New contradictory evidence or test results may reopen dependent assumptions. Verify hard requirements and execution evidence before delivery. Do not use runtime numeric self-scoring.

Skip full CRIT for simple lookups or fully specified low-ambiguity actions. Project-specific security, repository, tool, test, and release rules remain authoritative.
