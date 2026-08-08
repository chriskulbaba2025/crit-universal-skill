# FAQ

## Is this the official CRIT implementation?

No. This is an independent, unofficial cross-LLM implementation of the Context-Role-Interview-Task framework demonstrated publicly by Geoff Woods.

## Why not stop at Context, Role, Interview, Task?

Because the source session itself continues after the first draft. It demonstrates critique, a need to preserve previously good content during revisions, and top-down decomposition. The repository adds those operating controls plus explicit verification.

## Does CRIT always ask three questions?

No. It asks **up to** three, one at a time. Zero questions is correct when available context is already sufficient.

## Why can simple questions bypass CRIT?

Forcing a discovery interview onto arithmetic, a spelling correction, or a direct syntax question adds friction without improving the answer. The router exists to preserve the method for problems where context can actually change the outcome.

## Does the 95/100 gate prove the answer is correct?

No. It is a semantic self-review gate. Factual, technical, legal, financial, medical, or execution claims still need appropriate evidence and verification.

## Can I change the three-question cap?

Yes, but doing so changes a demonstrated behavior of the source method. If you publish a modified version, document it as a configuration change or fork rather than silently claiming exact fidelity.

## Can this run in any LLM?

Any LLM that can accept persistent or repeated instructions can use the semantic protocol. Automatic loading and compliance reliability vary by platform.

## Why include identity/context boundaries?

When a user models a scenario for someone else in first person, an AI system can misattribute that context. The core protocol explicitly separates represented third-party context from the actual user.
