from bank_server.main.application.dto.transaction_dto import TransactionDto
from bank_server.main.domain.entities.transaction import Transaction


class TransactionMapper:
    @staticmethod
    def to_dto(tx: Transaction) -> TransactionDto:
        return TransactionDto(
            transaction_id=tx.transaction_id,
            account_id=tx.account_id,
            amount=tx.amount,
            transaction_date=tx.transaction_date,
            status=tx.status,
            fraud_detected=tx.fraud_detected,
            transaction_type=tx.transaction_type,
            counterparty_name=tx.counterparty_name
        )

    @staticmethod
    def from_dto(dto: TransactionDto) -> Transaction:
        return Transaction(
            transaction_id=dto.transaction_id,
            account_id=dto.account_id,
            amount=dto.amount,
            transaction_date=dto.transaction_date,
            status=dto.status,
            fraud_detected=dto.fraud_detected,
            transaction_type=dto.transaction_type,
            counterparty_name=dto.counterparty_name,
        )
