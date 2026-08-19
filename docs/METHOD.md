# Method

## Root mechanism

CRIT is requirements discovery plus robustness control before solution generation.

The source method establishes **Context -> Role -> Interview -> Task**. CRIT Universal preserves that order semantically, while adding the operational controls required for repeated real-world use.

Version 1.1 adds a decision layer between discovery and Task compilation:

```text
Route
-> Context
-> Role
-> Interview
-> Decision Contract
-> Robustness Gate
-> Task
-> Produce
-> Critique
-> Preserve/Deepen
-> Verify
```

## Why robustness is separate from critique

**Robustness asks whether the foundation is stable enough to rely on.**

**Critique asks whether the candidate solution is good.**

A polished solution can still be fragile if one uncertain premise would reverse the recommendation.

## Context

Context distinguishes:

- facts;
- preferences;
- working assumptions;
- inferences;
- unknowns;
- constraints;
- anti-goals;
- evidence;
- prior attempts and available resources.

Approval establishes a requirement or preference. It does not establish an empirical fact.

## Role

Role establishes expertise, thinking function, relationship, and authority boundary.

The v1.1 invariant is:

> Role controls perspective, not conclusion.

## Interview

The interview remains capped at zero to three questions, one at a time.

Every question must pass the counterfactual test: if two materially different plausible answers would not change the Task, recommendation, constraints, or robustness state, the question is not worth asking.

The three-question cap is a cost ceiling, not an evidence threshold.

## Decision Contract

For substantial work, CRIT models:

- governing objective;
- decision owner;
- success condition;
- cost of being wrong;
- reversibility;
- evidence sufficiency;
- highest-leverage uncertain assumption;
- strongest credible disconfirming condition.

This prevents equal treatment of decisions with radically different downside or reversibility.

## Robustness Gate

CRIT does not challenge every assumption. It tests the uncertain premise most capable of changing the recommendation.

The core question is:

> If this assumption were false within a plausible range, would the recommendation materially change?

The answer controls one of three internal states:

- **PROCEED** - robust enough for the exposure;
- **CONDITIONAL** - useful but assumption-sensitive and bounded/reversible enough to proceed;
- **BLOCKED** - stronger evidence is required before responsible confidence.

## Evidence

CRIT Universal deliberately does not use a rigid source hierarchy.

Evidence is evaluated relative to each claim using:

- relevance;
- reliability;
- directness;
- recency;
- independence.

This avoids treating labels such as "authoritative source" or "direct observation" as automatically decisive.

## Preservation

CRIT distinguishes:

- `APPROVED_REQUIREMENT`;
- `ACCEPTED_FACT`;
- `WORKING_ASSUMPTION`.

Approved requirements remain locked against silent regression. New evidence can reopen only the dependent assumption or decision it materially affects.

## Verification

Runtime numeric self-grading was removed in v1.1.

The model now uses hard PASS/FAIL gates for problem fidelity, constraints, anti-goals, material assumptions, evidence discipline, authority boundaries, actionability, and honest robustness state.

Numeric scoring is reserved for external package evaluation and behavioral benchmarking.

## Behavioral validation

Package structure is not behavioral proof.

CRIT therefore separates:

1. **package conformance** - files, versions, invariants, links, adapter parity;
2. **behavioral conformance** - whether models route, interview, challenge, preserve, condition, block, and verify correctly across adversarial fixtures.

See `tests/behavioral/README.md`.

## Boundaries

CRIT does not guarantee factual correctness, legal/medical sufficiency, or execution quality. Direct evidence, tests, authoritative review, and human authorization remain required where the task demands them.
