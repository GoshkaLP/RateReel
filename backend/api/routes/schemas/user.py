from api.routes.schemas.base import BaseApiSchema
from api.services.schemas import user as service_schemas


class User(BaseApiSchema):
    username: str

    @classmethod
    def from_service_schema(cls, service_schema: service_schemas.User) -> "User":
        return cls(id=service_schema.id, username=service_schema.username)
