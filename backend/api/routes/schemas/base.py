from pydantic import BaseModel
from api.services.schemas.base import BaseServiceSchema
import uuid
from typing import TypeVar, Generic

ServiceSchema = TypeVar("ServiceSchema", bound=BaseServiceSchema)
ApiSchema = TypeVar("ApiSchema", bound="BaseApiSchema")


class BaseApiSchema(BaseModel, Generic[ServiceSchema]):
    @classmethod
    def from_service_schema(cls, service_schema: ServiceSchema) -> ApiSchema:
        return cls.model_validate(service_schema.model_dump())

    def to_service_schema(self) -> ServiceSchema:
        return ServiceSchema.model_validate(self.model_dump())


class IdApiSchemaMixin(BaseModel):
    id: uuid.UUID
