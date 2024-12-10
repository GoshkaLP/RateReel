from api.orm import models
from api.repo.base import BaseRepo


class MovieRepo(BaseRepo[models.Movie]):
    model = models.Movie
