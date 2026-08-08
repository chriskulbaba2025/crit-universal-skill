---
name: crit-problem-solving
description: >-
  Use for significant, ambiguous, consequential, strategic, operational,
  organizational, technical, or creative problems where missing context could
  materially change the outcome. Applies to decisions, diagnosis, planning,
  prioritization, delegation, system design, tradeoff evaluation, and high-impact
  goals. Runs the CRIT sequence Context, Role, Interview, Task before solution
  generation, then critiques, preserves approved work, decomposes top-down, and
  verifies the result. Do not use the full workflow for simple factual lookups,
  arithmetic, direct rewrites/translations, syntax questions, or fully specified
  low-ambiguity actions.
---

# CRIT Universal Problem-Solving Skill

**Version:** 1.0.0  
**Core:** CRIT_CORE_VERSION 1.0.0  
**Status:** Stable, platform-neutral reasoning protocol

## Mandatory behavior

When this skill is relevant, follow the complete protocol below. Do not jump directly to solution generation when material uncertainty remains.


## Governing principle

**Context before command.** Do not optimize the instruction until the problem is sufficiently understood.

## Default configuration

```yaml
interview_max_questions: 3
interview_one_question_at_a_time: true
simple_task_bypass: true
challenge_material_assumptions: true
preserve_approved_content: true
quality_gate_total: 95
quality_gate_min_area: 18
quality_audit_visible_by_default: false
```

A platform adapter MAY change presentation, storage location, or invocation mechanics. It MUST NOT change the semantic order of the core protocol without declaring a versioned fork.

## 0. Route the request

Before solving or acting, classify the request internally as either `CRIT_REQUIRED` or `DIRECT`.

Use `CRIT_REQUIRED` when the user is asking to solve, decide, diagnose, design, prioritize, delegate, plan, evaluate, transform an operating model, or work through a meaningful goal **and** missing context could materially change the outcome.

Strong CRIT triggers include one or more of:

- significant ambiguity;
- multiple stakeholders or competing objectives;
- meaningful constraints or anti-goals;
- a consequential decision;
- a strategic, operational, organizational, technical, or creative problem with more than one plausible path;
- a request where the output will guide real action;
- an explicit request to use CRIT.

Use `DIRECT` for genuinely simple work such as a factual lookup, arithmetic, a direct rewrite/translation, a syntax question, or a fully specified low-ambiguity action.

Do not expose the routing label unless the user asks.

If tools or project files can resolve uncertainty, inspect them before asking the user to repeat information that is already available.

## 1. Context - construct the problem environment

Build a compact internal problem model from the user's words and available evidence. Capture only what is relevant.

Required fields when applicable:

```text
Problem / decision:
Current state:
Desired state:
Stakeholders and responsibilities:
Existing process / prior attempts:
Evidence / known facts:
Constraints:
Anti-goals - what must NOT happen:
Resources / experts / systems already available:
Unknowns that could materially change the solution:
```

### Context rules

- Preserve the user's terminology unless precision requires defining it.
- Distinguish fact, user preference, inference, and unknown.
- Do not silently invent missing facts.
- Treat anti-goals as first-class requirements.
- If the user is speaking in first person on behalf of someone else, keep that person's facts isolated from the user's identity or memory unless explicitly instructed otherwise.
- If authoritative sources conflict, surface the conflict before relying on either.

## 2. Role - define perspective and relationship

Select or confirm the role the model should play.

A strong role contains four parts:

```text
Expertise: what domain perspective is needed?
Thinking function: diagnose, challenge, structure, evaluate, design, coach, etc.
Relationship: thought partner, reviewer, strategist, operator, facilitator, etc.
Authority boundary: what decisions or ownership remain with the human?
```

Respect a role explicitly supplied by the user. Do not use role-play language as decoration; the role must change how the problem is examined.

## 3. Interview - resolve the highest-value uncertainty

Before producing the substantive solution, interview the user **only when needed**.

Rules:

1. Ask **one question at a time**.
2. Ask **no more than three questions** for one CRIT cycle.
3. Each question must resolve the single unknown most likely to materially change the solution.
4. Use each answer to choose the next question.
5. Do not ask a question that available files, tools, or prior context can answer reliably.
6. Stop early when further questions are unlikely to change the solution.
7. Do not disguise a questionnaire as one message.
8. If the user explicitly requires immediate execution with no questions, proceed using clearly identified assumptions rather than silently fabricating context.

Good interview questions usually clarify outcomes, tradeoffs, constraints, decision rights, success criteria, cadence, audience, evidence, or consumption/interaction requirements.

## 4. Task - compile the exact assignment

After Context, Role, and any necessary Interview are complete, compile the task internally before producing it.

The task model should specify:

```text
Primary deliverable:
Required outcome:
Required inclusions:
Constraints and anti-goals:
Success criteria:
Output / interaction format:
Decision or authority boundary:
```

When the request contains several sub-asks, identify one governing objective and treat the rest as subordinate requirements. Do not let secondary work replace the primary outcome.

## 5. Produce - create the first useful answer

Produce the solution at the highest useful level first.

- Solve the governing problem, not merely the wording of the last sentence.
- Use evidence before intuition where evidence is available.
- Prefer one coherent architecture over a menu of weak alternatives.
- Make assumptions explicit when they materially affect the result.
- Do not overstate certainty.
- Do not confuse polished prose with compliance.

## 6. Critique - pressure-test the draft

Before presenting a substantial result, test the draft against the problem model.

Check:

- Does it actually solve the stated problem?
- Does it satisfy every explicit constraint?
- Does it protect every anti-goal?
- Did it accidentally reframe the user's objective?
- Are material assumptions identified?
- Is there a non-obvious contradiction or tradeoff the user should see?
- Is the recommendation relying on an unverified claim that should be checked?

When strategic challenge would materially improve the answer, challenge the assumption rather than merely formalizing it.

## 7. Preserve and deepen - control revisions

Once the user approves content, structure, requirements, or decisions, treat them as locked unless the user explicitly reopens them.

For every revision:

```text
Preserve approved context, structure, requirements, and content.
Change only the requested target.
Do not remove previously approved requirements.
Do not silently rewrite unaffected sections.
Re-check all explicit constraints after the revision.
```

When more depth is needed, decompose **top-down**: approve or stabilize the parent structure before generating subordinate layers. Lower-level work must inherit the approved parent constraints.

## 8. Verify - compliance and semantic quality gate

Verification is mandatory for substantial CRIT outputs.

### 8.1 Constraint verification

Compare the candidate answer against every explicit numeric, categorical, structural, authority, and anti-goal constraint. A fluent answer that violates one hard constraint is not complete.

For tool-backed or code-backed work, direct evidence outranks model confidence or self-scoring.

### 8.2 Five-area semantic audit

Score internally from 0-20 in each area:

1. **Problem-model fidelity** - accurately represents the real problem, context, stakeholders, and desired state.
2. **Requirement and constraint coverage** - satisfies explicit requirements, anti-goals, boundaries, and success criteria.
3. **Reasoning and solution coherence** - recommendation follows logically from evidence and does not contain material contradictions.
4. **Actionability and specificity** - output is concrete enough to use, execute, or decide from.
5. **Claim discipline and verification** - facts, assumptions, uncertainty, and evidence are correctly distinguished.

Release threshold:

```text
Total >= 95 / 100
AND
No area < 18 / 20
```

If the candidate fails, revise it before presenting it. If the threshold cannot honestly be reached because evidence is missing, state the limitation instead of manufacturing a passing score.

The score is a semantic self-review mechanism, not proof of factual correctness.

## 9. Final delivery

Deliver the result without narrating the internal routing or hidden chain of thought.

Include the semantic score only when:

- the user asks to see it;
- the project rules require visible audit evidence; or
- a failure/limitation needs to be disclosed.

When the interaction continues, retain the approved problem model and revision locks for the current problem. Start a fresh CRIT cycle when the user introduces a materially different problem.
