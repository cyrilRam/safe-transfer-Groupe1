from fastapi import Depends
from sqlalchemy.orm import Session

from bank_server.main.application.interfaces.Repositories.interface_transaction_repository import ITransactionRepository
from bank_server.main.application.interfaces.Services.interface_transactions import ITransactionService
from bank_server.main.application.interfaces.external_services.interface_client_safe_transfer import ISafeTransferClient
from bank_server.main.application.services.transaction_service import TransactionService
from bank_server.main.infrastructure.client_safe_transfer import SafeTransferClient
from bank_server.main.persitance.repositories.transaction_repository import TransactionRepository
from bank_server.main.webapi.dependencies.account_dependency import AccountDependency
from bank_server.main.webapi.dependencies.db_depends import DbDependency


class TransactionDependency:
    @staticmethod
    def get_transaction_service(
            db: Session = Depends(DbDependency.get_db_session)
    ) -> ITransactionService:
        transaction_repo: ITransactionRepository = TransactionRepository(db)
        safe_transfer_client: ISafeTransferClient = SafeTransferClient()
        account_service = AccountDependency.get_account_service(db)
        return TransactionService(transaction_repo, safe_transfer_client, account_service)
