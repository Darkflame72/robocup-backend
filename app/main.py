from typing import Any, Dict
import sentry_sdk
from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

sentry_sdk.init(dsn=settings.SENTRY_DSN)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Robocup Junior Scoring System.",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


def custom_openapi() -> Dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://lh6.googleusercontent.com/x2UaZCMiAO_1jYhft4JcXq8aYBOikH67GA6oWABUEsQTESCpjDlqX8vr1XFdLwPG2xd8vhkNyIrbFfHUYRoDckBJ9RQmNdaVK6DC4lckHRheX8OfDMQdSSkKER2C_AgUSw=w1280"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
async def docs_redirect() -> RedirectResponse:
    """Redirect home request to docs."""
    response = RedirectResponse(url="/docs")
    return response


asgi_app = SentryAsgiMiddleware(app)
