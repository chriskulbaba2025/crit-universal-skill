<!-- CRIT_CORE_VERSION: 1.0.0 -->
# Global Claude Code CRIT invocation rule

For every user prompt, evaluate whether the request is a qualifying problem before acting.

If the request is significant, ambiguous, consequential, strategic, operational, organizational, technical, or creative and missing context could materially change the outcome, invoke the `crit-problem-solving` skill before producing the substantive solution.

This includes decisions, root-cause diagnosis, planning, prioritization, delegation, architecture/system design, tradeoff evaluation, and high-impact goals.

Do not invoke the full CRIT workflow for simple factual lookups, arithmetic, direct rewrites/translations, syntax questions, or fully specified low-ambiguity actions.

When CRIT applies:

- inspect repository/files/tools before asking for information already available;
- ask zero to three interview questions, one at a time;
- do not produce the substantive solution until required context is sufficient;
- preserve approved content on revisions;
- verify every explicit constraint;
- apply the five-area semantic gate before substantial final delivery.

The project/repository's stricter safety, governance, authorization, and evidence rules remain in force and take precedence when applicable.
