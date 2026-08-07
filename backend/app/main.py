from fastapi import FastAPI
from app.database import Engine
from app.redis_client import RedisClient

App = FastAPI()

@App.get("/")
def Home():
    RedisClient.set("status" , "Running")
    return {
        "database":"connected",
        "redis":RedisClient.get("status")
    }