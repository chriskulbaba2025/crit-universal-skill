# LLM-Agnostic Use

CRIT Universal is a reasoning protocol, not a Claude-, ChatGPT-, Gemini-, Copilot-, or vendor-specific feature.

## Fastest installation on any LLM

If your LLM supports any persistent instruction surface, use:

```text
adapters/generic/SYSTEM_INSTRUCTIONS.md
```

Paste it into the product's:

- system prompt;
- custom instructions;
- project/workspace instructions;
- agent instructions;
- reusable prompt preset;
- persistent context or policy field.

If the platform supports `AGENTS.md`, use:

```text
adapters/agents-md/AGENTS.md
```

## If the LLM has no persistent instructions

At the start of a meaningful problem-solving conversation, provide the contents of:

```text
adapters/generic/SYSTEM_INSTRUCTIONS.md
```

Then give the problem normally.

The protocol does not depend on tool calling, a specific model family, or hidden implementation features.

## What the model should do

For consequential or ambiguous work, the model should:

```text
Context
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

It should bypass the full protocol for simple, fully specified work.

## Quick behavioral check

Give the model this prompt:

> We have already decided to replace our CRM. Tell me which platform to choose. The migration is expensive and we have not proven the CRM itself is the root problem.

A CRIT-enabled model should not blindly accept replacement as an established fact. It should recognize the decision-changing assumption, assess the downside/reversibility, and determine whether the recommendation can responsibly proceed.

## Model-neutral expectations

A compliant model should:

- ask only decision-changing questions;
- distinguish facts, preferences, assumptions, inferences, and unknowns;
- avoid letting a requested role predetermine the answer;
- test the highest-leverage uncertain assumption;
- match evidence depth to downside and reversibility;
- use PROCEED, CONDITIONAL, or BLOCKED internally;
- preserve approved requirements without freezing contradicted assumptions;
- verify hard requirements with PASS/FAIL gates;
- avoid numeric self-grading as proof of quality.

## Platform adapters

The adapters directory contains convenience packaging for common products. They all implement the same v1.1 semantic core. If your platform is not listed, use the generic adapter.

CRIT Universal is therefore **LLM-agnostic by design**: adapters change loading mechanics, not the reasoning protocol.
