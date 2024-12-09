from pydantic import BaseModel
import uuid


class BaseApiSchema(BaseModel):
    id: uuid.UUID
