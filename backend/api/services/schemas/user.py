from api.services.schemas.base import BaseServiceSchema
from api.services.schemas.role import Role
from api.services.schemas.review import Review
import uuid


class User(BaseServiceSchema):
    username: str
    password: str
    role_id: uuid.UUID
    role: Role
    reviews: list[Review]


class TokenCreate(BaseServiceSchema):
    username: str
    password: str


class UserCreate(TokenCreate):
    pass
