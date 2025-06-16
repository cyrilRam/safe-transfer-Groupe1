from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from safe_transfer_server.main.application.dto.interaction_ia_dto import SessionInteractionDto, RequestChatDto
from safe_transfer_server.main.application.interfaces.services.interface_chat_ia_service import IInteractionChatIaService
from safe_transfer_server.main.webapi.dependencies.chat_ia_depends import ChatIaDependency

router = APIRouter(prefix="/chat-ia", tags=["Chat IA"])
chat_ia_service_dependency = Annotated[IInteractionChatIaService, Depends(ChatIaDependency.get_ia_chat_service)]


@router.post("/ask", response_model=SessionInteractionDto, status_code=status.HTTP_200_OK)
def process_interaction( service: chat_ia_service_dependency,request: RequestChatDto):
    return service.process_interactions(request)


@router.get("/history/{session_id}", response_model=SessionInteractionDto)
def get_session_interaction( service: chat_ia_service_dependency,session_id: UUID):
    return service.get_interactions_by_session_id(session_id)
