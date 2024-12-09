from fastapi import Depends
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from api.orm.base import session_factory


def get_session():
    session = session_factory()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


DepSession = Annotated[Session, Depends(get_session)]
