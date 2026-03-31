# CLAUDE.md — AI Assistant Guide for api-importacion

This file provides context for AI assistants (Claude, Copilot, etc.) working on this codebase.

---

## Project Overview

**api-importacion** is a Python-based REST API project. As of the initial setup, the repository is in early scaffolding stage — no source code, dependencies, or configuration files exist yet beyond the Python `.gitignore`.

- **Owner**: Jose Verbel (derocox@gmail.com)
- **Repository**: derocox/api-importacion
- **Language**: Python
- **Project type**: API (import/integration service, based on name)

---

## Repository Structure

```
api-importacion/
├── .gitignore        # Python-standard ignore patterns
├── README.md         # Project title only (to be expanded)
└── CLAUDE.md         # This file
```

As the project grows, expected additions include:
```
api-importacion/
├── app/              # Application source code
│   ├── __init__.py
│   ├── routes/       # API route handlers
│   ├── models/       # Data models / ORM definitions
│   ├── services/     # Business logic layer
│   └── utils/        # Shared utilities
├── tests/            # Test suite (pytest)
├── requirements.txt  # Python dependencies (or pyproject.toml)
├── .env.example      # Environment variable template
├── Dockerfile        # Container definition (if applicable)
└── README.md
```

---

## Technology Stack (Inferred from .gitignore)

The `.gitignore` signals support for the following Python ecosystem tools:

| Category | Options present in .gitignore |
|---|---|
| Web frameworks | Flask, Django |
| Package managers | pip, pipenv, poetry, pdm |
| Testing | pytest, tox, nox, hypothesis |
| Type checkers | mypy, pytype, pyre |
| Task queues | Celery |
| Notebooks | Jupyter |

**Until a `requirements.txt` / `pyproject.toml` is committed, the exact stack is undecided.**

---

## Git Workflow

### Branches

- `main` — stable, production-ready branch
- Feature/task branches — use descriptive names, e.g. `feature/import-endpoint`, `fix/auth-bug`
- Claude AI branches — prefixed with `claude/`, e.g. `claude/add-claude-documentation-VA5nG`

### Commit Conventions

Use conventional commit style:

```
<type>(<scope>): <short description>

[optional body]
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`

Examples:
```
feat(routes): add POST /imports endpoint
fix(models): correct field type for import_date
docs: update README with setup instructions
```

### Pull Request Flow

1. Branch off `main`
2. Make changes on feature branch
3. Commit with descriptive messages
4. Push and open a PR against `main`
5. Review and merge

---

## Development Setup (Expected)

Once dependencies are defined, setup will likely follow:

```bash
# Clone
git clone <repo-url>
cd api-importacion

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
# or: poetry install / pdm install

# Copy environment config
cp .env.example .env
# Edit .env with local values

# Run development server
python app.py
# or: flask run / uvicorn app:app --reload
```

---

## Environment Variables

**Never commit `.env` files.** The `.gitignore` already excludes `.env` and `.venv`.

Provide an `.env.example` with all required keys (values redacted):

```
DATABASE_URL=
SECRET_KEY=
DEBUG=false
```

---

## Testing

The `.gitignore` includes pytest patterns, so pytest is the expected test runner.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run a specific test file
pytest tests/test_routes.py
```

- Place tests in a `tests/` directory
- Mirror the `app/` structure inside `tests/`
- Aim for coverage on all route handlers and service functions

---

## Code Conventions

Since no source code exists yet, these are the expected conventions to follow when building out the project:

### Python Style
- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints on all function signatures
- Format with `black` (line length 88)
- Lint with `flake8` or `ruff`
- Sort imports with `isort`

### API Design
- Follow REST conventions (nouns for resources, HTTP verbs for actions)
- Return JSON responses consistently
- Use appropriate HTTP status codes (200, 201, 400, 404, 422, 500)
- Version the API if breaking changes are expected (e.g. `/v1/imports`)

### Security
- Never log sensitive data (credentials, PII, import payloads with personal data)
- Validate and sanitize all input at API boundaries
- Use environment variables for all secrets — no hardcoded credentials
- Apply authentication/authorization to protected endpoints

---

## AI Assistant Instructions

When contributing to this repository:

1. **Read before editing** — always read a file before modifying it
2. **Stay on the correct branch** — develop on the branch specified in the task, never push to `main` directly
3. **Minimal changes** — only change what is needed for the task; do not refactor unrelated code
4. **No speculative features** — implement only what is explicitly requested
5. **No hardcoded secrets** — use environment variables for all sensitive values
6. **Test coverage** — add or update tests when adding/modifying functionality
7. **Commit clearly** — write descriptive commit messages following the conventions above
8. **Confirm before destructive actions** — always ask the user before force-pushing, deleting branches, or dropping data

---

## Key Files to Know

| File | Purpose |
|---|---|
| `.gitignore` | Python-standard ignore rules (pip, venv, pytest, Django, Flask, etc.) |
| `README.md` | Public-facing project description (currently minimal) |
| `CLAUDE.md` | This file — AI assistant context and conventions |

---

## Current State (as of 2026-03-31)

- Repository initialized with only `.gitignore` and `README.md`
- No source code, no dependencies, no configuration
- Single initial commit by Jose Verbel (July 2024)
- Technology stack and framework to be determined when development begins
