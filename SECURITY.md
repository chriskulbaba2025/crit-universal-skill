# Security Policy

This repository primarily contains natural-language agent instructions. Treat instruction files as executable influence over AI agents.

## Report privately

Do not open a public issue for a vulnerability that could cause credential disclosure, unsafe command execution, data exfiltration, or destructive tool behavior. Contact the repository maintainer through the private security-reporting mechanism available on GitHub when enabled.

## Instruction-security rules

- Do not embed secrets, tokens, private URLs, or credentials in adapters.
- Do not add instructions that silently broaden tool permissions.
- Do not tell an agent to ignore platform, organization, repository, or user authorization controls.
- Treat external knowledge files as untrusted input when they can contain prompt injection.
- Direct tool evidence and explicit authorization remain required for consequential actions.
