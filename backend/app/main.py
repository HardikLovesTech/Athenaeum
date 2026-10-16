from fastapi import FastAPI
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Engine
from app.redis_client import RedisClient
from app.api.v1.routes.auth import Router as AuthRouter
from app.api.v1.routes.users import Router as UsersRouter
from app.api.v1.routes.redis import Router as RedisRouter
from app.api.v1.routes.knowledge import Router as KnowledgeRouter
from app.api.v1.routes.search import Router as SearchRouter
from app.api.v1.routes.rag import Router as RAGRouter
from app.api.v1.routes.summary import Router as SummaryRouter

app = FastAPI(
    title="Athenaeum API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def Home():
    with Engine.connect() as Connection:
        Connection.execute(text("SELECT 1"))


    RedisClient.set("status" , "Running")

    return {
        "database":"connected",
        "redis":RedisClient.get("status")
    }


app.include_router(
    AuthRouter,
    prefix="/api/v1"
)

app.include_router(
    RedisRouter,
    prefix="/api/v1"
)


app.include_router(
    UsersRouter,
    prefix="/api/v1"
)

app.include_router(
    KnowledgeRouter,
    prefix="/api/v1"
)

app.include_router(
    SearchRouter,
    prefix="/api/v1"
)

app.include_router(
    RAGRouter,
    prefix="/api/v1"
)

app.include_router(
    SummaryRouter,
    prefix="/api/v1"
)