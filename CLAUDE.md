# CLAUDE.md — Project Guide for fluxopt-plot

## What is fluxopt-plot?

Companion package for [fluxopt](https://github.com/FBumann/fluxopt) providing
interactive plotly visualizations for energy system optimization results.

## Architecture

```
src/fluxopt_plot/
├── __init__.py       # Public API exports
├── py.typed          # PEP 561 marker
└── accessor.py       # PlotAccessor — main entry point for plotting
```

## Philosophy

- **uv is the single entry point** — no pip, no setuptools CLI, no tox
- **pyproject.toml is the single source of truth** — no setup.py/cfg, no tox.ini
- **src layout** — `src/fluxopt_plot/`, enforcing proper installation
- **hatchling + hatch-vcs** — version from git tags
- **ruff** replaces flake8, isort, pyupgrade, black
- **mypy strict** — enforced from day one
- **No lock file** — `uv.lock` is gitignored

## Common Commands

```bash
uv sync --group dev      # Install runtime + dev deps
uv run pytest -v         # Run tests
uv run ruff check .      # Lint
uv run ruff format .     # Format
uv run mypy src/         # Type check
```

## Code Style

- **Docstrings**: Google style, brief, on public functions
  - No types in docstrings (types live in signatures only)
  - Always include `Args` section when there are parameters
  - `Returns` / `Raises` only when non-obvious
- Python >= 3.12 — use modern syntax (PEP 604 unions `X | Y`, etc.)

## Commit & PR Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/) for **all** commit messages and PR titles:

```
<type>: <short summary>
```

Types: `feat`, `fix`, `refac`, `test`, `docs`, `chore`, `ci`, `perf`.
Optional scope: `feat(accessor): add flow rate chart`.

- **Commit messages**: `feat: add flow rate chart` (imperative, lowercase after colon)
- **PR titles**: same format
- No period at end, max ~70 chars
