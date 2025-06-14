from typing import Type
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session

from safe_transfer_server.main.application.interfaces.repositories.interface_transaction_repository import \
    IInterbankTransactionRepository
from safe_transfer_server.main.domain.entities.transactions import InterbankTransaction
from safe_transfer_server.main.domain.enums.transactions_enums import TransactionStatus
from safe_transfer_server.main.persistance.repositories.general_repository import GeneralRepository


class InterbankTransactionRepository(GeneralRepository[InterbankTransaction], IInterbankTransactionRepository):
    def __init__(self, session: Session):
        self.session = session
        super().__init__(session=session, model=InterbankTransaction)

    def get_by_sender_id(self, sender_id: UUID) -> list[Type[InterbankTransaction]]:
        return self.session.query(InterbankTransaction).filter(
            InterbankTransaction.user_source_id == sender_id
        ).all()

    def get_pending_transactions_for_user(self, user_id: UUID) -> list[Type[InterbankTransaction]]:
        return self.session.query(InterbankTransaction).filter(
            or_(
                InterbankTransaction.user_source_id == user_id,
                InterbankTransaction.user_dest_id == user_id
            ),
            or_(
                InterbankTransaction.status == TransactionStatus.PENDING_USER,
                InterbankTransaction.status == TransactionStatus.PENDING_RECIPIENT
            )
        ).all()

    def get_all_fraud_suspected_transactions(self) -> list[Type[InterbankTransaction]]:
        return self.session.query(InterbankTransaction).filter(
            InterbankTransaction.status == TransactionStatus.PENDING_FRAUD_CHECK
        ).all()
