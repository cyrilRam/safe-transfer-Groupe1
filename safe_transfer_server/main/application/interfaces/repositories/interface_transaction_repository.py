from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from safe_transfer_server.main.application.interfaces.repositories.interface_general_repository import \
    IGeneralRepository
from safe_transfer_server.main.domain.entities.transactions import InterbankTransaction


class IInterbankTransactionRepository(IGeneralRepository[InterbankTransaction], ABC):
    @abstractmethod
    def get_by_sender_id(self, sender_id: UUID) -> List[InterbankTransaction]:
        pass
