import json
from uuid import UUID

import aioredis
from fastapi import APIRouter
import os

from app.schemas.users import UserOut

redis_app1 = APIRouter()

redis = None

@redis_app1.on_event("startup")
async def startup_event():
    global redis
    redis_url = f"redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}"
    # Redis parolsiz ulanadi
    redis = aioredis.Redis.from_url(redis_url)

@redis_app1.on_event("shutdown")
async def shutdown_event():
    await redis.close()


# Helper function to get data from cache or fetch fresh data
async def get_cache_or_fetch(key: str, fetch_func, expire: int = 300):
    cached_data = await redis.get(key)
    if cached_data:
        return json.loads(cached_data)

    fresh_data = await fetch_func()

    # Helper function to convert UUIDs to string in the dictionary
    def uuid_to_str(data):
        if isinstance(data, dict):
            return {k: (str(v) if isinstance(v, UUID) else v) for k, v in data.items()}
        return data

    # Ensure that `fresh_data` is a list of Pydantic models (UserOut)
    fresh_data_dict = [uuid_to_str(UserOut.from_orm(user).dict()) for user in fresh_data]  # Convert ORM models to Pydantic models and then to dicts

    await redis.set(key, json.dumps(fresh_data_dict), ex=expire)
    return fresh_data_dict

