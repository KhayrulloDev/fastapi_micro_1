from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.user import user as user_crud
from app.db.db import get_db
from app.schemas.users import UserOut, GetUser, UserCreate

from app.redis_app import get_cache_or_fetch

router = APIRouter()


@router.post("/user-create", response_model=GetUser)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):

    if user_in.telegram_id != 0 and user_in.telegram_id // (10 ** (len(str(user_in.telegram_id)) - 1)) == 0:
        raise HTTPException(status_code=400, detail="Invalid Telegram ID. It cannot start with 0.")

    db_user = await user_crud.get_by_telegram_id(db, telegram_id=user_in.telegram_id)
    if db_user:
        return db_user

    new_user = await user_crud.create(db, obj_in=user_in)
    return new_user




@router.delete("/users", status_code=204)
async def delete_all_users(db: AsyncSession = Depends(get_db)):
    try:
        # Avval user_profit jadvalini tozalash
        await db.execute(text("DELETE FROM user_profit"))
        # Keyin users jadvalini tozalash
        await db.execute(text("DELETE FROM users"))
        await db.commit()
        return {"detail": "All users and associated data have been deleted"}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



@router.get("/users/", response_model=List[UserOut])
async def get_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    cache_key = f"users-{skip}-{limit}"

    # Function to fetch users from the database
    async def fetch_users():
        users = await user_crud.get_multi(db=db, skip=skip, limit=limit)
        return users
    # Use cache or fetch fresh data
    return await get_cache_or_fetch(cache_key, fetch_users)
