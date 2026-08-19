# Behavioral Conformance Tests

CRIT Universal separates **package conformance** from **behavioral conformance**.

The package validator proves that files, versions, links, adapters, and required invariants are aligned. It does not prove that an LLM follows the protocol correctly.

Behavioral fixtures define model-neutral expectations without requiring identical prose.

## Fixture contract

Each case in `cases.json` specifies:

```text
id
prompt
expected_route
expected_state
must_identify
must_not
max_questions
```

Optional fields can specify required evidence behavior, preservation behavior, or hard constraints.

## What should be evaluated

A model run should be judged on semantic behavior:

- correct `CRIT_REQUIRED` vs `DIRECT` routing;
- unnecessary interview questions avoided;
- decision-changing assumptions identified;
- false or performative challenge avoided;
- strongest credible disconfirming condition considered;
- correct PROCEED / CONDITIONAL / BLOCKED state;
- hard constraints and anti-goals protected;
- unsupported certainty avoided;
- approved requirements preserved;
- contradicted assumptions reopened;
- stable behavior under harmless paraphrase.

Exact wording is not part of conformance.

## Current automation

`scripts/validate-behavioral-fixtures.py` validates the fixture schema deterministically in CI.

Provider/model execution is intentionally separate because it requires model access and credentials. The fixture format is provider-neutral so the same cases can be run against Claude, GPT, Gemini, local models, or other LLMs.

A future benchmark result must report model/version, fixture revision, evaluator method, and pass rate. Do not label package conformance as reasoning-performance evidence.
