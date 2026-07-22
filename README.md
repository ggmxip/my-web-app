# my-web-app

A FastAPI web application with a full CI/CD pipeline.

## Quick start

```bash
uv sync --dev
uv run my-web-app
# or
uv run uvicorn my_web_app.main:app --reload
```

Open http://localhost:8000/docs

## CI/CD Pipeline

| Stage | Tool | Trigger |
|-------|------|---------|
| Lint | ruff | push/PR to main |
| Type check | mypy | push/PR to main |
| Test | pytest + coverage | push/PR to main |
| Security (SAST) | bandit | push/PR to main |
| Security (deps) | pip-audit | push/PR to main |
| Build package | uv build | push/PR to main |
| Docker image | Docker + ghcr.io | push to main + tags |
| PyPI publish | uv publish | tag v* |
| GitHub Release | softprops/action-gh-release | tag v* |

## License

MIT
