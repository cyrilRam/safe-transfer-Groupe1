from uuid import UUID

import requests

from safe_transfer_server.main.application.dto.interbank_transaction_dto import InterbankTransactionDto
from safe_transfer_server.main.application.interfaces.external_services.bank_client.interface_bank_client import \
    IBankClient
from safe_transfer_server.main.webapi.config.get_config import ConfigurationSafeTransfer


class BankHttpClient(IBankClient):
    BASE_URL = f"{ConfigurationSafeTransfer.get_bank_server_url()}"

    def validate_sender_transaction(self, transaction_id: UUID) -> bool:
        url = f"{self.BASE_URL}/transactions/{transaction_id}/safe-transfer/validation-sender"
        try:
            response = requests.put(url)
            return response.status_code == 200
        except Exception as e:
            print(f"[BankClient] Error validating sender transaction: {e}")
            return False

    def create_beneficiary_transaction(self, transaction: InterbankTransactionDto) -> bool:
        url = f"{self.BASE_URL}/transactions/safe-transfer/creation-beneficiary"
        try:
            payload = {
                "transaction_id": str(transaction.id),
                "account_id": str(transaction.user_beneficiary.account_id),
                "amount": transaction.amount,
                "transaction_type": "SAFETRANSFER_VIREMENT",
                "fraud_detected": False,
                "status": "VALIDATED",
                "counterparty_name": transaction.user_sender.name,
            }
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"[BankClient] Error creating beneficiary transaction: {e}")
            return False
