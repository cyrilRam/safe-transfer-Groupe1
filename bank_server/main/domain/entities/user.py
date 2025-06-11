import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from bank_server.main.persitance.config.database_connection import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    password = Column(String(255), nullable=False)
    iban = Column(String(34))
    bic = Column(String(11))
