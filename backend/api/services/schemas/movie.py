from api.services.schemas.base import (
    BaseServiceSchema,
    IdCreatedDeletedServiceSchemaMixin,
)
import uuid


class MovieCreate(BaseServiceSchema):
    title: str
    description: str
    imdb_rating: float


class Movie(MovieCreate, IdCreatedDeletedServiceSchemaMixin):
    logo_file_id: uuid.UUID
