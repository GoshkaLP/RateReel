from api.services.schemas.base import BaseServiceSchema
import uuid


class MovieCreate(BaseServiceSchema):
    title: str
    description: str
    imdb_rating: float


class Movie(MovieCreate):
    logo_file_id: uuid.UUID
