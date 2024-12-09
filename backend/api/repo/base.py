import uuid
from sqlalchemy.orm import Session
from sqlalchemy import sql
from typing import TypeVar, Generic, Type
from sqlalchemy import exc as sa_exc
from api.repo import exceptions as repo_exc

ModelType = TypeVar("ModelType")


class BaseRepo(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, session: Session):
        self.session = session

    def _base_select_stmt(self, **filters) -> sql.Select:
        stmt = sql.select(self.model)
        for attr, value in filters.items():
            stmt = stmt.where(getattr(self.model, attr) == value)
        return stmt

    def _apply_relations(self, stmt: sql.Select) -> sql.Select:
        return stmt

    def get_resource_by_filters(self, **filters) -> ModelType:
        stmt = self._base_select_stmt(**filters)
        stmt = self._apply_relations(stmt)
        try:
            return self.session.execute(stmt).unique().scalars().one()
        except sa_exc.NoResultFound as e:
            raise repo_exc.NotFoundError(orm_model_name=self.model.__name__) from e
        except sa_exc.MultipleResultsFound as e:
            raise repo_exc.MultipleFoundError(orm_model_name=self.model.__name__) from e

    def get_resources(self, **filters) -> list[ModelType]:
        stmt = self._base_select_stmt(**filters)
        stmt = self._apply_relations(stmt)
        return self.session.execute(stmt).unique().scalars().all()
