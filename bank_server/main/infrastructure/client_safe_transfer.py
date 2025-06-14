from uuid import UUID

import requests

from bank_server.main.application.interfaces.external_services.interface_client_safe_transfer import ISafeTransferClient
from bank_server.main.infrastructure.dto.safe_transfer_dto import TransactionSafeTransferDto
from bank_server.main.webapi.config.get_config import Configuration


class SafeTransferClient(ISafeTransferClient):
    def __init__(self):
        self.base_url = Configuration.get_st_server_url()

    def execute_safe_transfer(self, amount: float, user_id: UUID, beneficiary_mail: str) -> UUID:
        url = f"{self.base_url}/transactions"
        safe_transfer_dto = TransactionSafeTransferDto(user_bank_id_source=user_id, amount=amount,
                                                       user_dest_mail=beneficiary_mail, transaction_type="TRANSFER")
        response = requests.post(
            url,
            json=safe_transfer_dto.dict()
        )

        if response.status_code != 201:
            raise Exception(f"Safe transfer failed: {response.status_code} - {response.text}")

        created_transaction = response.json()
        return UUID(created_transaction["id"])
