import os
from functools import lru_cache
from pathlib import Path
from typing import Iterator

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


ENV_FILE = Path(__file__).resolve().parent.parent / ".env"


@lru_cache  # Least Recently Used.
def get_engine() -> Engine:
    database_url = os.environ.get("DATABASE_URL")
    if database_url is None:
        database_url = dotenv_values(ENV_FILE).get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("Set DATABASE_URL in the environment or employeecrud/.env")
    return create_engine(database_url, pool_pre_ping=True)


def get_session() -> Iterator[Session]:
    with Session(get_engine()) as session:
        yield session