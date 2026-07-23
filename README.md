# my-web-app

A FastAPI web application template with a full CI/CD pipeline built with GitHub Actions, Docker, and uv.

## Stack

- **Runtime:** Python 3.12+ / FastAPI / uvicorn
- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Build backend:** hatchling
- **CI/CD:** GitHub Actions (5 jobs)
- **Container:** Docker / GitHub Container Registry (ghcr.io)
- **Published to:** PyPI + GitHub Releases

## Quick start

```bash
# install uv (https://docs.astral.sh/uv/#getting-started)
uv sync --all-extras
uv run my-web-app
# or with hot reload:
uv run uvicorn my_web_app.main:app --reload
```

Open `/docs` in your browser for the interactive API docs.

## Project layout

```
src/my_web_app/
├── __init__.py
├── main.py       # FastAPI app, routes, uvicorn entry point
└── config.py     # pydantic-settings (env vars prefixed with MWA_)
tests/
├── __init__.py
└── test_main.py  # async integration tests via httpx
.github/workflows/
└── ci-cd.yml     # full pipeline
Dockerfile         # multi-stage, uv-based build
pyproject.toml     # dependencies, build config, tool settings
```

## CI/CD pipeline

| Job | What it does | Trigger |
|-----|-------------|---------|
| `quality` | ruff lint → mypy check → pytest + coverage → bandit SAST → pip-audit deps | Every push/PR to `main` |
| `build-package` | `uv build` → uploads sdist + wheel | After quality |
| `docker` | Multi-stage Docker build → push to ghcr.io with tags | After quality |
| `publish-pypi` | `uv publish` to PyPI | Only on `v*` tags |
| `release` | Creates GitHub Release with dist artifacts | Only on `v*` tags |

### Pipeline requires one secret

Go to **Settings → Secrets and variables → Actions → New repository secret** and add:

| Name | Value |
|------|-------|
| `PYPI_TOKEN` | A PyPI API token (create at [pypi.org/manage/account/token](https://pypi.org/manage/account/token/)) |

The built-in `GITHUB_TOKEN` is auto-generated per run — no setup needed.

## Release

```bash
git tag v0.1.0
git push origin v0.1.0
```

This triggers the full pipeline: quality checks → build → Docker push → PyPI publish → GitHub Release.

## Configuration

All settings use environment variables with the `MWA_` prefix:

| Variable | Default | Description |
|----------|---------|-------------|
| `MWA_APP_NAME` | `my-web-app` | App title (shown in API docs) |
| `MWA_DEBUG` | `false` | Enable debug mode and hot reload |
| `MWA_HOST` | `0.0.0.0` | Bind address |
| `MWA_PORT` | `8000` | Listen port |

## Local development

```bash
# install all deps (including dev)
uv sync --all-extras

# run tests with coverage
uv run pytest

# lint
uv run ruff check .

# type check
uv run mypy src/

# security scan
uv run bandit -r src/
uv run pip-audit
```

## License

MIT
