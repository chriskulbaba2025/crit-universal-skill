# Changelog

## 1.1.0 - Robustness & Evidence

- Added Decision Contract: objective, owner, success, cost of error, reversibility, and evidence sufficiency.
- Replaced discretionary assumption challenge with a highest-leverage Robustness Gate.
- Added strongest credible disconfirming condition and recommendation sensitivity testing.
- Added PROCEED, CONDITIONAL, and BLOCKED internal decision states.
- Added counterfactual interview-question test and clarified that the three-question cap is a cost ceiling.
- Replaced rigid evidence precedence with claim-relative evidence assessment: relevance, reliability, directness, recency, independence.
- Added approval-state separation: APPROVED_REQUIREMENT, ACCEPTED_FACT, WORKING_ASSUMPTION.
- Added evidence exception so new contradictory evidence can reopen dependent assumptions without silent regression.
- Removed runtime numeric self-scoring; verification now uses hard PASS/FAIL release gates.
- Added provider-neutral behavioral fixture framework and CI schema validation.
- Renamed the 99/100 score as package conformance, not reasoning-performance evidence.
- Added explicit LLM-agnostic installation and usage documentation.
- Updated all platform adapters to CRIT Core 1.1.0.

## 1.0.0

- Initial public release of CRIT Universal.
- Added platform-neutral core, routing, adapters, semantic package scorecard, validation, examples, and branding.
