from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class TransactionType(str, Enum):
    TRANSFER = "TRANSFER"
    WITHDRAWAL = "WITHDRAWAL"


class TransactionSafeTransferDto(BaseModel):
    user_bank_id_source: UUID
    user_dest_mail: str
    amount: float
    transaction_type: TransactionType
