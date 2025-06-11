from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Float, Boolean, DateTime, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from bank_server.main.domain.enums.transaction_enums import TransactionStatus, TransactionType
from bank_server.main.persitance.config.database_connection import Base


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)

    amount = Column(Float, nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)

    status = Column(Enum(TransactionStatus), nullable=False)
    fraud_detected = Column(Boolean, default=False)

    transaction_type = Column(Enum(TransactionType), nullable=False)
    counterparty_name = Column(String(255), nullable=True)
