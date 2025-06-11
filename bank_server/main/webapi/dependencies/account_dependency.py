from fastapi import Depends
from sqlalchemy.orm import Session

from bank_server.main.application.interfaces.Services.interafce_account_service import IAccountService
from bank_server.main.application.services.account_service import AccountService
from bank_server.main.persitance.config.database_connection import DataBaseConnection
from bank_server.main.persitance.repositories.account_repository import AccountRepository


class AccountDependency:
    @staticmethod
    def get_account_service(db: Session = Depends(DataBaseConnection().get_session)) -> IAccountService:
        return AccountService(AccountRepository(db))
