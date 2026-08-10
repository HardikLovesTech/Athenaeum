from fastapi import APIRouter

from app.services.redis_services import (
    DeleteValue,
    Exists,
    GetValue,
    SetValue,
)


Router = APIRouter(
    prefix="/redis",
    tags=["Redis"],
)


@Router.get("/health")
def RedisHealth():
    SetValue(
        Key="athenaeum:test",
        Value="Redis is working",
        ExpirationSeconds=60,
    )

    Value = GetValue(
        Key="athenaeum:test",
    )

    return {
        "status": "Redis service is running",
        "value": Value,
        "exists": Exists("athenaeum:test"),
    }