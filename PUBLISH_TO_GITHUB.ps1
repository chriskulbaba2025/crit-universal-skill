param(
    [string]$Owner = "chriskulbaba2025",
    [string]$RepoName = "crit-universal-skill"
)

$ErrorActionPreference = "Stop"
$Repo = "$Owner/$RepoName"
$Description = "Cross-LLM CRIT problem-solving skill: Context, Role, Interview, Task, with critique, revision control, decomposition, and verification."

Write-Host "Validating package..."
python scripts/validate-package.py
if ($LASTEXITCODE -ne 0) { throw "Package validation failed." }

Write-Host "Checking GitHub authentication..."
gh auth status
if ($LASTEXITCODE -ne 0) { throw "GitHub CLI is not authenticated." }

$exists = $false
gh repo view $Repo *> $null
if ($LASTEXITCODE -eq 0) { $exists = $true }
if ($exists) { throw "Repository $Repo already exists. Refusing to overwrite it." }

if (-not (Test-Path ".git")) {
    git init -b main
}

git add .
$pending = git status --porcelain
if ($pending) {
    git commit -m "feat: publish CRIT Universal v1.0.0"
}

Write-Host "Creating public repository $Repo..."
gh repo create $Repo --public --source . --remote origin --push --description $Description
if ($LASTEXITCODE -ne 0) { throw "Repository creation failed." }

gh repo edit $Repo --add-topic ai --add-topic llm --add-topic agent-skills --add-topic claude-code --add-topic chatgpt --add-topic gemini --add-topic prompt-engineering --add-topic problem-solving --add-topic decision-making

gh release create v1.0.0 --repo $Repo --title "CRIT Universal v1.0.0" --notes "Initial stable public release: cross-LLM CRIT protocol, adapters, validation, documentation, and branding."

Write-Host "Published: https://github.com/$Repo"
