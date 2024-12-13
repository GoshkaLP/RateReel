from api.routes.schemas.base import BaseApiSchema, IdApiSchemaMixin
from api.services.schemas import movie as service_schemas
from api.utils.files import generate_movie_logo_file_path


class MovieMulti(BaseApiSchema[service_schemas.Movie], IdApiSchemaMixin):
    title: str
    imdb_rating: float
    logo_file_url: str

    @classmethod
    def from_service_schema(cls, service_schema: service_schemas.Movie) -> "MovieMulti":
        return cls(
            id=service_schema.id,
            title=service_schema.title,
            imdb_rating=service_schema.imdb_rating,
            logo_file_url=generate_movie_logo_file_path(service_schema.logo_file_id),
        )


class MovieDetailed(MovieMulti, IdApiSchemaMixin):
    description: str

    @classmethod
    def from_service_schema(cls, service_schema: service_schemas.Movie) -> "MovieMulti":
        return cls(
            id=service_schema.id,
            title=service_schema.title,
            imdb_rating=service_schema.imdb_rating,
            logo_file_url=generate_movie_logo_file_path(service_schema.logo_file_id),
            description=service_schema.description,
        )


class MovieCreate(BaseApiSchema[service_schemas.MovieCreate]):
    title: str
    description: str
    imdb_rating: float
