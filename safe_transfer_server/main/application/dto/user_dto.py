from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
    id: Optional[UUID] = None
    id_bank_user: UUID
    name: str
    mail: EmailStr
    phone: Optional[str] = None
    account_id: Optional[UUID] = None
