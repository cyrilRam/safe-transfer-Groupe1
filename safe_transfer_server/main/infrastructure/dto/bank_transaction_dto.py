from datetime import datetime
from typing import Optional, Literal
from uuid import UUID

from pydantic import BaseModel, Field


class BankTransactionDto(BaseModel):
    transaction_id: Optional[UUID] = None
    account_id: UUID
    amount: float
    transaction_date: Optional[datetime] = None
    status: Literal["VALIDATED"] = Field(default="VALIDATED")
    fraud_detected: bool = False
    transaction_type: Literal["SAFETRANSFER_VIREMENT"] = Field(default="SAFETRANSFER_VIREMENT")
    counterparty_name: Optional[str] = None
