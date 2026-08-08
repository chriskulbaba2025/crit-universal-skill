# Contributing

Contributions are welcome through pull requests.

## Requirements

1. Preserve the semantic order of the CRIT core unless the proposal is explicitly a versioned protocol change.
2. Keep platform-specific mechanics in adapters rather than hard-coding them into the core.
3. Do not weaken the one-question-at-a-time or three-question maximum without documenting the behavioral change.
4. Preserve the distinction between semantic self-review and factual/executable evidence.
5. Run `python scripts/validate-package.py` before opening a pull request.
6. Update `CHANGELOG.md` for user-visible behavior changes.
7. Do not add copyrighted source transcripts, paid course materials, private reports, credentials, or client data.

A pull request should state the problem, changed behavior, affected adapters, and validation result.
