# Troubleshooting

## The model answers immediately instead of interviewing

The likely cause is that the platform did not load the persistent adapter, or the router judged the task as sufficiently specified. First verify the adapter is active. Then test with a clearly ambiguous, consequential problem.

## It asks all three questions at once

The adapter is not being followed closely enough. Reinforce: **one question at a time; never bundle a questionnaire**.

## It keeps interviewing forever

The three-question cap is hard. Stop after three or earlier when no remaining unknown can materially change the solution.

## Revisions destroy good earlier work

Use the preservation rule: approved content is locked; change only the requested target; re-check all hard constraints after revision.

## It gives a 95+ score despite missing evidence

That is invalid use of the quality gate. Missing evidence must be disclosed; the model must not manufacture a passing score.

## Claude Code does not see the skill

Confirm the file path is exactly `~/.claude/skills/crit-problem-solving/SKILL.md` or `.claude/skills/crit-problem-solving/SKILL.md`. If the top-level skills directory was created after the current session began, restart Claude Code. See the official skills documentation.

## Gemini CLI does not load the context

Run `/memory show` and confirm the expected `GEMINI.md` appears in loaded context. Project and global context files use different locations.
