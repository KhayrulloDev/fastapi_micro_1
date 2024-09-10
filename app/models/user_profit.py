import uuid
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base
from FastAPIServices.app.models.users import User

class UserProfit(Base):
    __tablename__ = "user_profit"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    hour_profit = Column(BigInteger, nullable=False)
    main_profit = Column(BigInteger, nullable=False)

    # Relationship to User
    user = relationship("User", back_populates="profits")

