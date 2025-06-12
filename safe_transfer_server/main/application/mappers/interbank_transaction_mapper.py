from safe_transfer_server.main.application.dto.interbank_transaction_dto import InterbankTransactionDto
from safe_transfer_server.main.domain.entities.transactions import InterbankTransaction


class InterbankTransactionMapper:
    @staticmethod
    def to_dto(entity: InterbankTransaction) -> InterbankTransactionDto:
        return InterbankTransactionDto(
            id=entity.id,
            user_source_id=entity.user_source_id,
            user_dest_id=entity.user_dest_id,
            amount=entity.amount,
            status=entity.status,
            transaction_date=entity.transaction_date,
            double_auth_source=entity.double_auth_source,
            double_auth_dest=entity.double_auth_dest,
            transaction_type=entity.transaction_type,
            source_code=entity.source_code,
            dest_code=entity.dest_code,
        )

    @staticmethod
    def from_dto(dto: InterbankTransactionDto) -> InterbankTransaction:
        return InterbankTransaction(
            id=dto.id,
            user_source_id=dto.user_source_id,
            user_dest_id=dto.user_dest_id,
            amount=dto.amount,
            status=dto.status,
            transaction_date=dto.transaction_date,
            double_auth_source=dto.double_auth_source,
            double_auth_dest=dto.double_auth_dest,
            transaction_type=dto.transaction_type,
            source_code=dto.source_code,
            dest_code=dto.dest_code,
        )
