from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from bank_server.main.persitance.config.database_connection import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    balance = Column(Float, nullable=False)
    opening_date = Column(DateTime, default=datetime.utcnow)
    name = Column(String(255), nullable=False)
