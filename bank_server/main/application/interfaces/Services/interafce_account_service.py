from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from bank_server.main.application.dto.account_dto import AccountDto


class IAccountService(ABC):
    @abstractmethod
    def get_all_accounts(self) -> List[AccountDto]:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: UUID) -> AccountDto:
        pass

    @abstractmethod
    def create_account(self, dto: AccountDto) -> AccountDto:
        pass

    @abstractmethod
    def update_account(self, dto: AccountDto) -> AccountDto:
        pass

    @abstractmethod
    def delete_account(self, account_id: UUID) -> AccountDto:
        pass
