from api.routes.schemas.base import BaseApiSchema, IdApiSchemaMixin
from api.services.schemas import user as service_schemas
from pydantic import BaseModel


class User(BaseApiSchema[service_schemas.User], IdApiSchemaMixin):
    username: str
    role_name: str

    @classmethod
    def from_service_schema(cls, service_schema: service_schemas.User) -> "User":
        return cls(
            id=service_schema.id,
            username=service_schema.username,
            role_name=service_schema.role.title,
        )


class TokenCreate(BaseApiSchema[service_schemas.TokenCreate]):
    username: str
    password: str


class UserCreate(BaseApiSchema[service_schemas.UserCreate]):
    username: str
    password: str
