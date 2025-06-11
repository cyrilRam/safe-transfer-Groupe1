from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class AccountDto(BaseModel):
    id: Optional[UUID] = None
    user_id: UUID
    balance: float
    opening_date: Optional[datetime] = None
    name: str
