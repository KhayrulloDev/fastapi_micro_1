from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.schemas.tasks import ChannelResponse

from app.utils.tasks_utils import fetch_channels

tasks = APIRouter()

@tasks.get("/channels", response_model=List[ChannelResponse])
async def get_channels():
    # Fetch the channels using async HTTP request
    channels = await fetch_channels()
    return channels