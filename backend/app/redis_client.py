import redis
from app.core.config import RedisHost, RedisPort

RedisClient = redis.Redis(
    host=RedisHost,
    port=int(RedisPort),
    decode_responses=True
)


