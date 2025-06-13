from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from bank_server.main.application.interfaces.Repositories.interface_general_repository import IGeneralRepository
from bank_server.main.domain.entities.transaction import Transaction


class ITransactionRepository(IGeneralRepository[Transaction], ABC):
    @abstractmethod
    def get_all_by_account_id(self, account_id: UUID) -> List[Transaction]:
        pass

    @abstractmethod
    def get_by_safe_transfer_id(self, safe_transfer_id: UUID) -> Transaction:
        pass
