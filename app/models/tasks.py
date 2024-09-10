import uuid
from sqlalchemy import Column, String, BigInteger, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base
import datetime


class Task(Base):
    __tablename__ = "tasks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_name = Column(String, nullable=False)
    task_price = Column(BigInteger, nullable=False)
    task_description = Column(String, nullable=True)
    status = Column(Boolean, nullable=False, default=False)
    task_time = Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    task_link = Column(String, nullable=True)