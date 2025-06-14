from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from bank_server.main.domain.enums.transaction_enums import TransactionStatus, TransactionType


class TransactionDto(BaseModel):
    transaction_id: Optional[UUID] = None
    account_id: UUID
    amount: float
    transaction_date: Optional[datetime] = None
    status: TransactionStatus
    fraud_detected: bool = False
    transaction_type: TransactionType
    counterparty_name: Optional[str] = None
