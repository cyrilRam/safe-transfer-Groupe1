from typing import List
from uuid import UUID

from bank_server.main.application.dto.account_dto import AccountDto
from bank_server.main.application.interfaces.Repositories.interface_account_repository import IAccountRepository
from bank_server.main.application.interfaces.Services.interafce_account_service import IAccountService
from bank_server.main.application.mappers.account_mapper import AccountMapper


class AccountService(IAccountService):
    def __init__(self, repository: IAccountRepository):
        self.repository = repository

    def get_all_accounts(self) -> List[AccountDto]:
        return [AccountMapper.to_dto(acc) for acc in self.repository.get_all()]

    def get_account_by_id(self, account_id: UUID) -> AccountDto:
        return AccountMapper.to_dto(self.repository.get_by_id(account_id))

    def create_account(self, dto: AccountDto) -> AccountDto:
        return AccountMapper.to_dto(self.repository.create(AccountMapper.from_dto(dto)))

    def update_account(self, dto: AccountDto) -> AccountDto:
        return AccountMapper.to_dto(self.repository.update(AccountMapper.from_dto(dto)))

    def delete_account(self, account_id: UUID) -> AccountDto:
        return AccountMapper.to_dto(self.repository.delete(account_id))
