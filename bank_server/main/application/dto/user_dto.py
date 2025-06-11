from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
    id: Optional[UUID] = None
    name: str
    email: EmailStr
    phone: Optional[str] = None
    password: str
    iban: Optional[str] = None
    bic: Optional[str] = None
