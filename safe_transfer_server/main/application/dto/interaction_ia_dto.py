from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class RequestChatDto(BaseModel):
    id: Optional[UUID] = None
    prompt: str
    session_id: Optional[UUID] = None


class InteractionDto(BaseModel):
    id: Optional[UUID] = None
    prompt: str
    response: str
    created_at: Optional[datetime] = None
    session_id: Optional[UUID] = None


class SessionInteractionDto(BaseModel):
    session_id: Optional[UUID] = None
    interactions: List[InteractionDto]
