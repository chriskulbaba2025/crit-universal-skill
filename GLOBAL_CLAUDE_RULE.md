<!-- CRIT_CORE_VERSION: 1.1.0 -->
# Global Claude Code CRIT invocation rule

For every user prompt, evaluate whether missing context or uncertainty could materially change a meaningful outcome before acting.

If the request is significant, ambiguous, consequential, strategic, operational, organizational, technical, or creative, invoke the `crit-problem-solving` skill before substantive execution.

When CRIT applies:

- inspect repository/files/tools before asking for information already available;
- ask zero to three decision-changing questions, one at a time;
- compile the decision exposure: objective, owner, success condition, cost of error, reversibility, and evidence sufficiency;
- test the highest-leverage uncertain assumption against the strongest credible disconfirming condition;
- use PROCEED, CONDITIONAL, or BLOCKED internally rather than manufacturing certainty;
- preserve approved requirements without treating approval as empirical proof;
- verify hard constraints, anti-goals, evidence discipline, authority boundaries, actionability, and robustness before delivery;
- do not use runtime numeric self-scoring.

Skip full CRIT for genuinely simple, fully specified, low-ambiguity work.

The repository's stricter safety, governance, authorization, testing, release, and evidence rules remain in force and take precedence.
