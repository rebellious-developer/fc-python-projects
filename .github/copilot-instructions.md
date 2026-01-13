# Copilot Instructions for fc-python-projects

## Project Overview

This is a project created to hold the `Python Projects` module code that I created as part of the Data Science training/certification course with Future Connect. The repo will contain basic Python scripts demonstrating the fundamental programming concepts and techniques necessary for the assigned exercises.

## Project Structure

Currently minimal structure:
- [README.md](README.md) — This file.
- [requirements.txt](requirements.txt) — Defines external Python dependencies (none currently).
- [.python-version](.python-version) — Project Python version (3.12).
- [.gitignore](.gitignore) — Files and directories ignored by git.
- [.editorconfig](.editorconfig) — Editor configuration (PEP8 / indentation rules).
- [.github/copilot-instructions.md](.github/copilot-instructions.md) — Project Copilot usage guidance.


## Development Environment
1. Each exercise uses it's own virtual environment.
2. Python version 3.12 specified in `.python-version`.
3. Each exercise is in it's own sub-folder named by the exercise number and topic.

### System Configuration
- **OS**: Ubuntu LTS
- **Version Control**: Git (latest via PPA)
- **SSH**: ed25519 key authentication for GitHub
- **CLI Tools**: GitHub CLI (gh) for repository management

### Git Configuration
- **Default branch**: `main`
- **Line endings**: LF (Unix-style) - configured globally with `core.eol lf`
- **Global ignore**: Uses `~/.git` ignore file for system-wide exclusions
- **Remote**: origin → `git@github.com:rebellious-developer/fc-python-activities.git`

## Key Workflows

### Creating New Python Files
When adding Python code to this project:
1. Add new Python files in the root or appropriate sub-folder.
2. Use descriptive filenames indicating the exercise purpose (e.g., `01_hello_world.py`).
3. Update `requirements.txt` only if external packages are needed.

### Git Workflow
Standard workflow used in this project:
```bash
git add <files>
git commit -m "descriptive message"
git push origin main
```

For new features, the project owner uses GitHub CLI for repo operations.

## Project Context

This is a **training/certification project** under the Future Connect organization:
- Focus on demonstrating basic Python development
- Additions should be educational and incrementally build skills
- Keep structure simple and beginner-friendly

## Python Guidelines

When adding Python code:
- Start with simple console applications (`print()` statements are fine)
- No frameworks or complex dependencies initially
- Add `requirements.txt` only when external packages are needed
- Use descriptive filenames that indicate the exercise purpose (e.g., `01_hello_world.py`, `02_variables.py`)

## Testing Approach

No formal testing framework currently configured. When adding tests:
- Use Python's built-in `unittest` or `pytest` for simplicity
- Create a `tests/` directory when needed
- Document test execution in README.md
