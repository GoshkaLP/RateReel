from pydantic import BaseModel, ConfigDict
import uuid
import datetime


class BaseServiceSchema(BaseModel):
    id: uuid.UUID
    created_at: datetime.datetime
    deleted: bool

    model_config = ConfigDict(from_attributes=True)
