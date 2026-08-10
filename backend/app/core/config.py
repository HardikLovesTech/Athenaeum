import os

from dotenv import load_dotenv

load_dotenv()

def GetRequiredEnvironmentVariable(Name: str) -> str:
    Value = os.getenv(Name)

    if Value is None:
        raise RuntimeError(
            f"Required environment variable --> '{Name} <-- is not set"
        )
    return Value

PostgresHost = GetRequiredEnvironmentVariable("POSTGRES_HOST")
PostgresPort = GetRequiredEnvironmentVariable("POSTGRES_PORT")
PostgresDatabase = GetRequiredEnvironmentVariable("POSTGRES_DB")
PostgresUser = GetRequiredEnvironmentVariable("POSTGRES_USER")
PostgresPassword = GetRequiredEnvironmentVariable("POSTGRES_PASSWORD")

RedisHost = GetRequiredEnvironmentVariable("REDIS_HOST")
RedisPort = GetRequiredEnvironmentVariable("REDIS_PORT")


AccessTokenExpireMinutes = int(GetRequiredEnvironmentVariable("ACCESS_TOKEN_EXPIRE_MINUTES"))
SecretKey = GetRequiredEnvironmentVariable("SECRET_KEY")
RefreshTokenExpireDays = int(GetRequiredEnvironmentVariable("REFRESH_TOKEN_EXPIRE_DAYS"))