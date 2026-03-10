# fluxopt-plot

Interactive [plotly](https://plotly.com/python/) visualization for [fluxopt](https://github.com/FBumann/fluxopt) energy system models.

[![PyPI](https://img.shields.io/pypi/v/fluxopt-plot)](https://pypi.org/project/fluxopt-plot/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

> **Early development** — the API may change between releases.

## Installation

```bash
pip install fluxopt-plot
```

## Development

Requires [uv](https://docs.astral.sh/uv/) and Python >= 3.12.

```bash
uv sync --group dev      # Install deps
uv run pytest -v         # Run tests
uv run ruff check .      # Lint
uv run ruff format .     # Format
uv run mypy src/         # Type check
```

## License

MIT
