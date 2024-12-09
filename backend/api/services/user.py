from api.repo.user import UserRepo
from api.orm import models
from api.services.schemas import user as schemas
from api.services.base import BaseService


class UserService(BaseService[models.User, schemas.User]):
    model = models.User
    service_schema = schemas.User
    repo = UserRepo
