# app/config.py

import os

REDIS_HOST = os.getenv("REDIS_HOST", "192.168.101.228")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", 'your_redis_password')
