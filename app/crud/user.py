from app.crud.base import CRUDBase
from app.models.users import User, UserProfit
from app.schemas.users import UserCreate, UserUpdate,ToBenefit, GetBenefit

user = CRUDBase[User, UserCreate, UserUpdate](User)
# Create a CRUD instance for UserProfit
user_profit_crud = CRUDBase[UserProfit, ToBenefit, ToBenefit](UserProfit)

