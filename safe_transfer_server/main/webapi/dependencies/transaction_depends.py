from fastapi import Depends
from sqlalchemy.orm import Session

from safe_transfer_server.main.application.interfaces.repositories.interface_transaction_repository import \
    IInterbankTransactionRepository
from safe_transfer_server.main.application.interfaces.services.interface_transaction_service import \
    IInterbankTransactionService
from safe_transfer_server.main.application.services.interbank_transaction_service import InterbankTransactionService
from safe_transfer_server.main.persistance.repositories.interbank_transaction_repository import \
    InterbankTransactionRepository
from safe_transfer_server.main.webapi.dependencies.db_depends import DbDependency


class InterbankTransactionDependency:
    @staticmethod
    def get_transaction_service(
            db: Session = Depends(DbDependency.get_db_session)
    ) -> IInterbankTransactionService:
        repo: IInterbankTransactionRepository = InterbankTransactionRepository(db)
        return InterbankTransactionService(repo)
