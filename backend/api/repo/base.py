import uuid
from sqlalchemy.orm import Session
from sqlalchemy import sql
from typing import TypeVar, Generic, Type

ModelType = TypeVar("ModelType")


class BaseRepo(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, session: Session):
        self.session = session

    def _base_select_stmt(self, **filters) -> sql.Select:
        stmt = sql.select(self.model)
        for attr, value in filters.items():
            stmt = stmt.where(attr=value)
        return stmt

    def _apply_relations(self, stmt: sql.Select) -> sql.Select:
        return stmt

    def get_resource_by_filters(self, resource_id: uuid.UUID, **filters) -> ModelType:
        stmt = self._base_select_stmt(**filters)
        stmt = stmt.where(self.model.id == resource_id)
        stmt = self._apply_relations(stmt)
        return self.session.execute(stmt).unique().scalars().one()

    def get_resources(self, **filters) -> list[ModelType]:
        stmt = self._base_select_stmt(**filters)
        stmt = self._apply_relations(stmt)
        return self.session.execute(stmt).unique().scalars().all()
