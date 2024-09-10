from pydantic import BaseModel
from uuid import UUID


class ChannelResponse(BaseModel):
    id: UUID
    channel_name: str
    channel_id: str