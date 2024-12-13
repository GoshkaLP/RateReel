from api.services.schemas.base import BaseServiceSchema
from api.services.schemas.role import Role
import uuid
from pydantic import BaseModel


class User(BaseServiceSchema):
    username: str
    password: str
    role_id: uuid.UUID
    role: Role


class TokenCreate(BaseModel):
    username: str
    password: str


class UserCreate(TokenCreate):
    pass
