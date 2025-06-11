from sqlalchemy.orm import Session

from bank_server.main.application.interfaces.Repositories.interface_account_repository import IAccountRepository
from bank_server.main.domain.entities.account import Account
from bank_server.main.persitance.repositories.general_repository import GeneralRepository


class AccountRepository(GeneralRepository[Account], IAccountRepository):
    def __init__(self, session: Session):
        super().__init__(session, Account)
