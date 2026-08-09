from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import Engine
from app.redis_client import RedisClient

app = FastAPI(
    title="Athenaeum API",
    version="1.0.0"
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