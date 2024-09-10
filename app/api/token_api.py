from fastapi import APIRouter, Depends, HTTPException

from app.schemas.users import Token, RefreshTokenRequest, TelegramIDRequest
from app.utils.utils import verify_token, create_access_token, create_refresh_token

token_router = APIRouter()


@token_router.post("/token", response_model=Token)
async def login_for_access_token(telegram_id_req: TelegramIDRequest):
    telegram_id = telegram_id_req.telegram_id

    # Bu yerda siz telegram_id asosida foydalanuvchini tekshirish jarayonini amalga oshirishingiz mumkin.
    user_data = {"telegram_id": telegram_id}

    # Access va refresh tokenlarni yaratish
    access_token = await create_access_token(data=user_data)
    refresh_token = await create_refresh_token(data=user_data)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@token_router.post("/refresh-token", response_model=Token)
async def refresh_access_token(refresh_token_req: RefreshTokenRequest):
    refresh_token = refresh_token_req.refresh_token

    # Refresh tokenni tekshirish
    try:
        payload = await verify_token(refresh_token)
        telegram_id = payload.get("telegram_id")
        if telegram_id is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    except HTTPException:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    # Yangi access va refresh tokenlarni yaratish
    user_data = {"telegram_id": telegram_id}
    access_token = await create_access_token(data=user_data)
    new_refresh_token = await create_refresh_token(data=user_data)

    return {
        "access_token": access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }
