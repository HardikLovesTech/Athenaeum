from app.redis_client import RedisClient


def SetValue(
    Key: str,
    Value: str,
    ExpirationSeconds: int | None = None,
) -> bool:

    if ExpirationSeconds is None:
        return bool(
            RedisClient.set(
                Key,
                Value,
            )
        )

    return bool(
        RedisClient.set(
            Key,
            Value,
            ex=ExpirationSeconds,
        )
    )


def GetValue(
    Key: str,
) -> str | None:

    Value = RedisClient.get(Key)

    if Value is None:
        return None

    if isinstance(Value, bytes):
        return Value.decode("utf-8")

    return Value

def DeleteValue(
    Key: str,
) -> int:

    return int(
        RedisClient.delete(Key)
    )


def Exists(
    Key: str,
) -> bool:

    return bool(
        RedisClient.exists(Key)
    )