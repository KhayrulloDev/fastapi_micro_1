from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.users import CreateBenefit
from app.utils.utils import verify_token

from fastapi.security import  HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.user import user_profit_crud, user as user_crud
from app.db.db import get_db
from app.schemas.users import GetBenefit, ToBenefit, BenefitList



security = HTTPBearer()
benefit_router = APIRouter()



@benefit_router.post('/to-benefit', response_model=GetBenefit)
async def update_benefit(
    user_benefit: ToBenefit,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials
    current_user = await verify_token(token)

    # Retrieve the user by telegram_id
    user = await user_crud.get_by_telegram_id(db, current_user["telegram_id"])

    # Retrieve the benefit data using the user's ID
    db_benefit = await user_profit_crud.get_by_user_id(db, user_id=user.id)

    # If the benefit is not found, raise an error
    if not db_benefit:
        raise HTTPException(status_code=404, detail="Benefit not found or access denied")

    # Update the benefit with the new data (add the incoming profit to the existing one)
    db_benefit.main_profit += user_benefit.main_profit

    # Commit the changes to the database
    db.add(db_benefit)
    await db.commit()
    await db.refresh(db_benefit)

    return db_benefit


@benefit_router.get("/benefit/me", response_model=GetBenefit)
async def get_my_benefit(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials
    current_user = await verify_token(token)

    user = await user_crud.get_by_telegram_id(db, current_user["telegram_id"])

    user_benefit = await user_profit_crud.get_by_user_id(db, user_id=user.id)

    # Agar benefit topilmasa, yangi benefit profilini yaratish
    if user_benefit is None:
        new_benefit_data = CreateBenefit(
            id=uuid.uuid4(),
            user_id=user.id,  # Topilgan yoki yangi yaratilgan foydalanuvchi ID sini ishlatish
            main_profit=0,
            hour_profit=0
        )
        user_benefit = await user_profit_crud.create(db=db, obj_in=new_benefit_data)

    return user_benefit

@benefit_router.get('/benefit-list/', response_model=List[BenefitList])
async def benefit_list(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    benefits = await user_profit_crud.get_multi(db, skip=skip, limit=limit)
    return benefits