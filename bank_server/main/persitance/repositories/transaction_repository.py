from typing import Type, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from bank_server.main.application.interfaces.Repositories.interface_transaction_repository import ITransactionRepository
from bank_server.main.domain.entities.transaction import Transaction
from bank_server.main.persitance.repositories.general_repository import GeneralRepository


class TransactionRepository(GeneralRepository[Transaction], ITransactionRepository):

    def __init__(self, session: Session):
        super().__init__(session, Transaction)

    def get_all_by_account_id(self, account_id: UUID) -> list[Type[Transaction]]:
        return self.session.query(Transaction).filter_by(account_id=account_id).all()

    def get_by_safe_transfer_id(self, safe_transfer_id: UUID) -> Optional[Transaction]:
        return self.session.query(Transaction).filter_by(safe_transaction_id=safe_transfer_id).first()
