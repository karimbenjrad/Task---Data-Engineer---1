from contextlib import contextmanager
from typing import Callable, ContextManager

from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session

from source.exceptions.database_exceptions import CreateAllTablesError, YieldingSessionError

Base = declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url, echo=True)
        self.session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine)
        )

    def create_database(self) -> None:
        try:
            Base.metadata.create_all(self.engine)
        except exc.SQLAlchemyError as database_init_error:
            raise CreateAllTablesError from database_init_error

    @contextmanager
    def session(self) -> Callable[..., ContextManager[Session]]:
        session = self.session_factory()
        try:
            yield session
        except YieldingSessionError as yield_session_error:
            session.rollback()
            raise YieldingSessionError from yield_session_error
        finally:
            session.close()