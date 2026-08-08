# Example - Coding architecture

**User:** Our worker retries are unreliable. Fix the architecture.

A CRIT-enabled coding agent should inspect the repository before asking the user for facts that code/tests can reveal. Context should capture current retry behavior, failure modes, existing tests, invariants, and prohibited changes. Role should be a diagnostic software architect/implementer bounded by repository governance.

If repository evidence leaves a material product decision unresolved, ask one question. Otherwise ask zero. Compile the exact Task only after the architecture boundary is understood, then execute under the repository's own testing and release rules.
