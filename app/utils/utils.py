import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
import uuid


SECRET_KEY = "yasfsadfhldsajfhp238r283z8p2mP@(*$R$*#PRU#_$)TR*_#GTU#POGIJUH#POGMJH#PGOIU#J%"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
REFRESH_TOKEN_EXPIRE_DAYS = 7

async def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    if "id" not in to_encode:
        to_encode["id"] = str(uuid.uuid4())  # Yoki haqiqiy foydalanuvchi ID ni qo'ying
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    if "id" not in to_encode:
        to_encode["id"] = str(uuid.uuid4())  # Yoki haqiqiy foydalanuvchi ID ni qo'ying
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def verify_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if "id" not in decoded_jwt:
            raise HTTPException(status_code=400, detail="Invalid token: 'id' not found")
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")