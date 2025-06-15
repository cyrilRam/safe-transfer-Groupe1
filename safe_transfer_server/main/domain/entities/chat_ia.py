from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from safe_transfer_server.main.persistance.config.database_connection import Base


class InteractionIa(Base):
    __tablename__ = "interactions_ia"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    session_id = Column(UUID(as_uuid=True), nullable=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
