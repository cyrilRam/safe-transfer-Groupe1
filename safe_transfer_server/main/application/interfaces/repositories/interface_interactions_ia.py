from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from safe_transfer_server.main.application.interfaces.repositories.interface_general_repository import \
    IGeneralRepository
from safe_transfer_server.main.domain.entities.chat_ia import InteractionIa


class IInteractionRepository(IGeneralRepository[InteractionIa], ABC):
    @abstractmethod
    def get_all_by_session_id(self, session_id: UUID) -> List[InteractionIa]:
        """
        Retrieve all interactions linked to a specific session.
        """
        pass
