import uuid
from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base



class UserProfit(Base):
    __tablename__ = "user_profit"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    hour_profit = Column(BigInteger, nullable=True)
    main_profit = Column(BigInteger, nullable=True)

    # Relationship to User
    user = relationship("User", back_populates="profits")

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, unique=True, nullable=True)
    fullname = Column(String, nullable=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False, index=True)

    # Relationship to UserProfit
    profits = relationship("UserProfit", back_populates="user", cascade="all, delete-orphan")