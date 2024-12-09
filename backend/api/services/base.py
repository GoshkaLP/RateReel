from typing import TypeVar, Generic, Type
from pydantic import BaseModel
from api.repo.base import BaseRepo
from sqlalchemy.orm import Session
import uuid

ModelType = TypeVar("ModelType")
ServiceSchema = TypeVar("ServiceSchema", bound=BaseModel)
Repo = TypeVar("Repo", bound=BaseRepo)


class BaseService(Generic[ModelType, ServiceSchema]):
    model: Type[ModelType]
    service_schema: Type[ServiceSchema]
    repo: Type[Repo]

    def __init__(self, session: Session):
        self.session = session

    def get_resource_by_filters(self, resource_id: uuid.UUID, **filters) -> ModelType:
        result = self.repo(self.session).get_resource_by_filters(
            resource_id=resource_id, **filters
        )
        return self.service_schema.model_validate(result)
