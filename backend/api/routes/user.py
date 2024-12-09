from fastapi import APIRouter
import uuid
from api.orm.session import DepSession
from api.services.user import UserService
from api.routes.schemas import user as api_schemas

router = APIRouter(prefix="/user")


@router.get("/{resource_id}")
def get_user(resource_id: uuid.UUID, session: DepSession):
    user = UserService(session).get_resource_by_filters(resource_id=resource_id)
    return api_schemas.User.from_service_schema(user)
