from uuid import UUID

from pydantic import BaseModel

from bank_server.main.domain.enums.transaction_enums import TransactionType


class TransactionSafeTransferDto(BaseModel):
    user_bank_id_source: UUID
    user_dest_mail: str
    amount: float
    transaction_type: TransactionType
