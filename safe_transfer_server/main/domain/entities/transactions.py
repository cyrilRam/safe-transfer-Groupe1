from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Float, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from safe_transfer_server.main.domain.enums.transactions_enums import TransactionStatus, TransactionType
from safe_transfer_server.main.persistance.config.database_connection import Base


class InterbankTransaction(Base):
    __tablename__ = "interbank_transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_source_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user_dest_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(TransactionStatus), nullable=False, default=TransactionStatus.PENDING_USER)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    double_auth_source = Column(Boolean, default=False)
    double_auth_dest = Column(Boolean, default=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    source_code = Column(String(10), nullable=True)
    dest_code = Column(String(10), nullable=True)
