from fastapi import APIRouter, status
import uuid
from api.orm.session import DepSession
from api.services.user import UserService
from api.routes.schemas import user as api_schemas

router = APIRouter(prefix="/api/token")


@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create_token(payload: api_schemas.TokenCreate, session: DepSession):
    return UserService(session).auth_user(payload)
