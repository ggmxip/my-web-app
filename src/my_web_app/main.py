from collections.abc import Mapping

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from my_web_app.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/")
async def root() -> Mapping[str, str]:
    return {"status": "ok", "app": settings.app_name}


@app.get("/health")
async def health() -> JSONResponse:
    return JSONResponse(content={"status": "healthy"})


def run() -> None:
    uvicorn.run(
        "my_web_app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )


if __name__ == "__main__":
    run()
