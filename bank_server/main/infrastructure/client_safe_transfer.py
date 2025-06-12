import uuid
from uuid import UUID

from bank_server.main.application.dto.transaction_dto import TransactionSafeTransferDto
from bank_server.main.application.interfaces.external_services.interface_client_safe_transfer import ISafeTransferClient


class SafeTransferClient(ISafeTransferClient):
    def execute_safe_transfer(self, amount: float, user_id: UUID, beneficiary_mail: str) -> UUID:
        # TODO
        safe_transfer_dto = TransactionSafeTransferDto(user_bank_id_source=user_id, amount=amount,
                                                       user_dest_mail=beneficiary_mail, transaction_type="TRANSFER")
        return uuid.uuid4()
