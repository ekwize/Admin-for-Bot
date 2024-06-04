import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import v1
from settings import settings


def create_app():
    app = FastAPI()

    app.include_router(v1)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    