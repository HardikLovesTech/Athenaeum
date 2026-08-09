from collections.abc import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.db.database import Engine


SessionLocal = sessionmaker(
    bind=Engine,
    class_=Session,
    autoflush=False,
    autocommit=False,
)


def GetDatabase() -> Generator[Session , None , None]:
    Database = SessionLocal()

    try:
        yield Database
    finally:
        Database.close()