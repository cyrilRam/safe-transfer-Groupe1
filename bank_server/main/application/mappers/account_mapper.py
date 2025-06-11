from bank_server.main.application.dto.account_dto import AccountDto
from bank_server.main.domain.entities.account import Account


class AccountMapper:
    @staticmethod
    def to_dto(account: Account) -> AccountDto:
        return AccountDto(
            id=account.id,
            user_id=account.user_id,
            balance=account.balance,
            opening_date=account.opening_date,
            name=account.name
        )

    @staticmethod
    def from_dto(dto: AccountDto) -> Account:
        return Account(
            id=dto.id,
            user_id=dto.user_id,
            balance=dto.balance,
            opening_date=dto.opening_date,
            name=dto.name
        )
