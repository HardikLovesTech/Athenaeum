from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


from app.core.config import (
    PostgresDatabase,
    PostgresHost,
    PostgresPassword,
    PostgresPort,
    PostgresUser
)

DATABASE_URL = (
    f"postgresql://{PostgresUser}:{PostgresPassword}"
    f"@{PostgresHost}:{PostgresPort}/{PostgresDatabase}"
)

class Base(DeclarativeBase):
    pass

Engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    )