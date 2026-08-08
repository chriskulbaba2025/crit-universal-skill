#!/usr/bin/env bash
set -euo pipefail
OWNER="${1:-chriskulbaba2025}"
REPO_NAME="${2:-crit-universal-skill}"
REPO="$OWNER/$REPO_NAME"
DESC="Cross-LLM CRIT problem-solving skill: Context, Role, Interview, Task, with critique, revision control, decomposition, and verification."

python scripts/validate-package.py
gh auth status
if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "Repository $REPO already exists. Refusing to overwrite it." >&2
  exit 1
fi

if [[ ! -d .git ]]; then git init -b main; fi
git add .
if [[ -n "$(git status --porcelain)" ]]; then
  git commit -m "feat: publish CRIT Universal v1.0.0"
fi

gh repo create "$REPO" --public --source . --remote origin --push --description "$DESC"
gh repo edit "$REPO" --add-topic ai --add-topic llm --add-topic agent-skills --add-topic claude-code --add-topic chatgpt --add-topic gemini --add-topic prompt-engineering --add-topic problem-solving --add-topic decision-making
gh release create v1.0.0 --repo "$REPO" --title "CRIT Universal v1.0.0" --notes "Initial stable public release: cross-LLM CRIT protocol, adapters, validation, documentation, and branding."
echo "Published: https://github.com/$REPO"
