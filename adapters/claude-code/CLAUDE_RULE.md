<!-- CRIT_CORE_VERSION: 1.0.0 -->
# CRIT Universal Router

For every user request, first determine whether it is a qualifying problem.

Invoke `crit-problem-solving` for any significant, ambiguous, consequential, strategic, operational, organizational, technical, or creative problem where missing context could materially change the outcome. This includes decisions, root-cause diagnosis, planning, prioritization, delegation, system design, tradeoff evaluation, and high-impact goals.

Do not invoke the full workflow for simple factual questions, arithmetic, direct rewrites/translations, syntax lookups, or fully specified low-ambiguity actions.

When invoked, use the sequence **Context -> Role -> Interview -> Task -> Produce -> Critique -> Preserve/Deepen -> Verify**. Interview with zero to three questions, one at a time, asking only what can materially change the solution. Inspect available files/tools before asking the user for facts that can be verified directly.

Approved material is locked during revisions. Substantial final outputs require the five-area semantic gate of at least 95/100 with no area below 18/20; direct evidence outranks self-scoring.


## Claude Code execution note

When CRIT is required, invoke the `crit-problem-solving` skill. Repository-specific governance, security, test, release, and authorization instructions remain authoritative and should be incorporated into Context and Task rather than overwritten by this skill.
