from fastapi import APIRouter, status
from api.orm.session import get_session
from api.services.user import UserService
from api.routes.schemas import user as api_schemas

router = APIRouter(prefix="/api/token", tags=["token"])


@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create_token(payload: api_schemas.TokenCreate):
    with get_session() as session:
        return UserService(session).auth_user(payload.to_service_schema())
