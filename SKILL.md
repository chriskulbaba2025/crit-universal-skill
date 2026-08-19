---
name: crit-problem-solving
description: >-
  Use for significant, ambiguous, consequential, strategic, operational,
  organizational, technical, or creative problems where missing context or
  uncertainty could materially change the outcome. Runs Context, Role, Interview,
  Decision Contract, Robustness Gate, Task, Produce, Critique, Preserve/Deepen,
  and Verify. Tests the highest-leverage uncertain assumption, scales evidence
  requirements to the cost and reversibility of error, and uses PROCEED,
  CONDITIONAL, or BLOCKED states instead of manufacturing certainty. Bypass the
  full workflow for simple factual lookups, arithmetic, direct rewrites or
  translations, syntax questions, and fully specified low-ambiguity actions.
---

# CRIT Universal Problem-Solving Skill

**Version:** 1.1.0  
**Core:** CRIT_CORE_VERSION 1.1.0  
**Status:** Stable, LLM-agnostic reasoning protocol

## Mandatory behavior

When this skill is relevant, follow the semantic protocol in `core/CRIT_CORE.md`. The canonical runtime sequence is:

```text
ROUTE
→ CONTEXT
→ ROLE
→ INTERVIEW
→ DECISION CONTRACT
→ ROBUSTNESS GATE
→ TASK
→ PRODUCE
→ CRITIQUE
→ PRESERVE / DEEPEN
→ VERIFY
→ DELIVER
```

## Governing invariants

1. **Context before command.**
2. **Role controls perspective, not conclusion.**
3. Ask only interview questions whose plausible answers could change the Task, recommendation, constraints, or robustness state.
4. Three interview questions is a cost ceiling, not proof that evidence is sufficient.
5. Distinguish facts, user preferences, working assumptions, inferences, and unknowns.
6. Evaluate evidence by relevance, reliability, directness, recency, and independence relative to the claim; do not rely on a fixed source hierarchy.
7. For substantial work, define cost of error, reversibility, evidence sufficiency, the highest-leverage uncertain assumption, and the strongest credible disconfirming condition.
8. Test whether the recommendation materially changes if the highest-leverage uncertain assumption is false within a plausible range.
9. Use `PROCEED`, `CONDITIONAL`, or `BLOCKED` internally to match certainty to robustness and decision exposure.
10. User approval locks requirements and preferences, not empirical truth.
11. New contradictory evidence may reopen the dependent assumption or decision without silently rewriting approved history.
12. Verification uses hard PASS/FAIL release gates. Do not use numeric runtime self-scoring.
13. Repository-, project-, safety-, security-, authorization-, and evidence-specific rules remain authoritative.

## Routing

Use full CRIT when missing context or uncertainty could materially change a meaningful outcome. Use direct handling for simple, fully specified, low-ambiguity work.

Inspect available tools, files, project context, and reliable sources before asking the user to repeat information.

## Interview rule

Before asking a question:

```text
Can available evidence answer this?
If no, imagine two materially different plausible answers.
Would either change the Task, recommendation, constraint set, or robustness state?
If no → do not ask.
```

Ask no more than three questions, one at a time.

## Decision Contract

For substantial work, compile internally:

```text
Governing objective:
Decision owner:
Success condition:
Cost of being wrong: LOW | MEDIUM | HIGH
Reversibility: REVERSIBLE | PARTIAL | HARD_TO_REVERSE
Evidence sufficiency: SUFFICIENT | PARTIAL | INSUFFICIENT
Highest-leverage uncertain assumption:
Strongest credible disconfirming condition:
```

## Robustness Gate

Test only the uncertainty most capable of changing the recommendation.

```text
Assumption:
Why it matters:
Evidence for:
Evidence against:
Strongest credible disconfirming condition:
Falsifier / weakening evidence:
Consequence if wrong:
```

Then ask:

> If this assumption were false within a plausible range, would the recommendation materially change?

Use:

- `PROCEED` when sufficiently robust;
- `CONDITIONAL` when assumption-sensitive but bounded/reversible enough to proceed;
- `BLOCKED` when decision-changing uncertainty plus downside or irreversibility requires stronger evidence.

## Preservation states

```text
APPROVED_REQUIREMENT
ACCEPTED_FACT
WORKING_ASSUMPTION
```

Do not let approval turn an empirical assertion into a fact. If new evidence contradicts dependent work, flag and reopen only what the evidence affects.

## Verification

Before substantial delivery, all applicable gates must PASS:

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

If a gate cannot pass because evidence is missing, do not manufacture a passing answer. Deliver conditionally or state that the decision is blocked.

Do not expose hidden chain-of-thought. Show the user only the reasoning summary, evidence, assumptions, conditions, and conclusions needed to evaluate or act on the result.
