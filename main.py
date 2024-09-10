# main.py

import os
import json
import aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.redis_app import redis_app1
from app.api.benefit import benefit_router
from app.api.token_api import token_router
from app.api.users import router
from app.api.tasks import tasks
from debug_toolbar.middleware import DebugToolbarMiddleware
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    DebugToolbarMiddleware,
    panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
)


# Include routers
app.include_router(benefit_router)
app.include_router(tasks)
app.include_router(token_router)
app.include_router(router)
app.include_router(redis_app1)
