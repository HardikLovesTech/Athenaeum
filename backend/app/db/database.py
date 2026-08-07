from sqlalchemy import create_engine

DATABASE_URL = "postgresql://athenaeum:athenaeum123@localhost:5432/athenaeum"

Engine = create_engine(DATABASE_URL)