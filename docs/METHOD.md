# Method

## Root mechanism

CRIT is most useful when treated as **requirements discovery before solution generation**, not as an acronym to paste in front of a task.

The source demonstration shows the human progressively transferring the problem model into the LLM: circumstances, stakeholders, desired outcomes, constraints, working preferences, cadence, and decision rights. The Task arrives only after that transfer is substantially complete.

## Four cognitive functions

### Context
Construct the problem environment. Strong Context contains the desired outcome **and** anti-goals: what must not happen.

### Role
Define perspective and relationship. Role is not costume. It establishes expertise, thinking function, how the model should behave relative to the human, and where its authority stops.

### Interview
Resolve material unknowns. The source prompt explicitly used one question at a time and no more than three questions. The point is not diligence for its own sake; each question should change the solution if answered differently.

### Task
Compile the assignment only after discovery. In the source demonstration, the final Task sentence was comparatively simple because the intelligence had already been transferred through Context, Role, and Interview.

## What CRIT Universal adds

A reusable implementation cannot stop at the first draft. The source session also demonstrated three operational needs:

1. **Critique** - the human evaluates the draft and provides specific feedback.
2. **Preservation** - revision instructions must protect already-approved material from silent regression.
3. **Decomposition** - stabilize the high-level structure before generating subordinate layers.

The source also showed why an explicit **verification** pass matters: a stated 30-minute meeting ceiling was not fully honored by the first model draft. Fluent output is not the same as constraint compliance.

CRIT Universal therefore uses the full cycle:

```text
Route -> Context -> Role -> Interview -> Task -> Produce -> Critique -> Preserve/Deepen -> Verify
```

## Leadership parallel

The method maps closely to competent delegation:

| CRIT function | Delegation question |
|---|---|
| Context | Do they understand the situation? |
| Role | Do they understand how they are expected to contribute? |
| Interview | Have the important questions been asked before acting? |
| Task | Is the required outcome clear? |

The public source conversation itself explicitly connects learning CRIT with learning to lead people. This repository treats that as an application of the framework, not proof that every leadership problem should be delegated to an LLM.

## Boundaries

CRIT does not automatically guarantee adversarial thinking, factual correctness, or execution quality. If a task requires assumption challenge, source verification, tests, legal/medical review, or independent audit, those requirements must be included and actually performed.

The five-area score in this repository is a semantic self-review. It is never a substitute for direct evidence.
