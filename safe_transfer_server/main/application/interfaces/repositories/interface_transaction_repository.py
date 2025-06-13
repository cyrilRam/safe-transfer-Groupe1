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

    @abstractmethod
    def get_pending_transactions_for_user(self, user_id: UUID) -> List[InterbankTransaction]:
        pass

    @abstractmethod
    def get_all_fraud_suspected_transactions(self) -> List[InterbankTransaction]:
        pass
