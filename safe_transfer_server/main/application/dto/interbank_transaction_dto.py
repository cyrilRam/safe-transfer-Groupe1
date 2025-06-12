from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from safe_transfer_server.main.domain.enums.transactions_enums import TransactionStatus, TransactionType


class InterbankTransactionDto(BaseModel):
    id: Optional[UUID] = None
    user_source_id: UUID
    user_dest_id: UUID
    amount: float
    status: TransactionStatus
    transaction_date: Optional[datetime] = None
    double_auth_source: bool = False
    double_auth_dest: bool = False
    transaction_type: TransactionType
    source_code: Optional[str] = None
    dest_code: Optional[str] = None


class InterbankTransactionCreationDto(BaseModel):
    user_bank_id_source: UUID
    user_dest_mail: str
    amount: float
    transaction_type: TransactionType
