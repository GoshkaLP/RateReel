from api.routes.schemas.base import BaseApiSchema
from api.services.schemas import user as service_schemas
from pydantic import BaseModel


class User(BaseApiSchema):
    username: str
    role_name: str

    @classmethod
    def from_service_schema(cls, service_schema: service_schemas.User) -> "User":
        return cls(
            id=service_schema.id,
            username=service_schema.username,
            role_name=service_schema.role.title,
        )


class TokenCreate(BaseModel):
    username: str
    password: str

    def to_service_schema(self) -> service_schemas.TokenCreate:
        return service_schemas.TokenCreate(**self.model_dump())


class UserCreate(TokenCreate):
    def to_service_schema(self) -> service_schemas.UserCreate:
        return service_schemas.UserCreate(**self.model_dump())
