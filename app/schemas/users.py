import uuid

from pydantic import BaseModel


from pydantic import BaseModel, Field
import uuid

class BenefitList(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    hour_profit: int
    main_profit: int

    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class UserOut(BaseModel):
    id: uuid.UUID
    username: str
    fullname: str
    telegram_id: int

    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class UserCreate(BaseModel):
    username: str
    telegram_id: int
    fullname: str

    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class UserUpdate(BaseModel):
    username: str
    telegram_id: int
    fullname: str

    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class GetUser(BaseModel):
    id: uuid.UUID
    username: str
    telegram_id: int
    fullname: str = Field(..., alias="fullname")

    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class GetBenefit(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    main_profit: int

    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class CreateBenefit(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    hour_profit: int
    main_profit: int
    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class ToBenefit(BaseModel):
    main_profit: int
    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class TelegramIDRequest(BaseModel):
    telegram_id: int
    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak

class RefreshTokenRequest(BaseModel):
    refresh_token: str
    class Config:
        from_attributes = True  # Bu joyga from_attributes = True ni qo'shish kerak


class UserCreate(BaseModel):
    username: str
    telegram_id: int
    fullname: str

    class Config:
        from_orm = True

class UserUpdate(BaseModel):
    username: str
    telegram_id: int
    fullname: str

    class Config:
        from_orm = True

class GetUser(BaseModel):
    id: uuid.UUID
    username: str
    telegram_id: int
    fullname: str = Field(..., alias="fullname")

    class Config:
        from_orm = True

class GetBenefit(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    main_profit: int

    class Config:
        from_orm = True


class CreateBenefit(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    hour_profit: int
    main_profit: int
    class Config:
        from_orm = True

class ToBenefit(BaseModel):
    main_profit: int
    class Config:
        from_orm = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    class Config:
        from_orm = True


class TelegramIDRequest(BaseModel):
    telegram_id: int
    class Config:
        from_orm = True

class RefreshTokenRequest(BaseModel):
    refresh_token: str