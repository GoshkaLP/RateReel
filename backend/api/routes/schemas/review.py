import uuid

from api.routes.schemas.base import BaseApiSchema, IdApiSchemaMixin
from api.services.schemas import review as service_schemas


class Review(BaseApiSchema[service_schemas.Review], IdApiSchemaMixin):
    username: str
    movie_id: uuid.UUID
    content: str
    rating: float
