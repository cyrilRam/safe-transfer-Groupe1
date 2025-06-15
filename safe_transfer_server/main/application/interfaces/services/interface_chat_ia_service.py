from abc import ABC, abstractmethod
from uuid import UUID

from safe_transfer_server.main.application.dto.interaction_ia_dto import SessionInteractionDto, RequestChatDto


class IInteractionChatIaService(ABC):
    @abstractmethod
    def process_interactions(self, request: RequestChatDto) -> SessionInteractionDto:
        """
        Process  interaction. If session_id is None, a new session will be created.
        """
        pass

    @abstractmethod
    def get_interactions_by_session_id(self, session_id: UUID) -> SessionInteractionDto:
        """
        Retrieve all interactions associated with the given session_id.
        """
        pass
