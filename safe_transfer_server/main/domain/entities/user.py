from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from safe_transfer_server.main.persistance.config.database_connection import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_bank_user = Column(UUID(as_uuid=True), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    mail = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    account_id = Column(UUID(as_uuid=True))
