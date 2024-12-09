from api.services.schemas.base import BaseServiceSchema
import uuid


class Review(BaseServiceSchema):
    user_id: uuid.UUID
    movie_id: uuid.UUID
    content: str
    rating: float
    approved: bool
