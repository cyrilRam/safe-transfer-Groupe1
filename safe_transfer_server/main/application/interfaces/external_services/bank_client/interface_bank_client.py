from abc import ABC, abstractmethod
from uuid import UUID

from safe_transfer_server.main.application.dto.interbank_transaction_dto import InterbankTransactionDto


class IBankClient(ABC):
    @abstractmethod
    def validate_sender_transaction(self, transaction_id: UUID) -> bool:
        """
        Calls the sender's bank API to validate the transaction and debit the account.

        :param transaction_id: The ID of the transaction to validate.
        :return: True if validation is successful, False otherwise.
        """
        pass

    @abstractmethod
    def create_beneficiary_transaction(self, transaction: InterbankTransactionDto) -> bool:
        """
        Calls the beneficiary's bank API to create and record the mirrored transaction,
        and credit the beneficiary's account.

        :param transaction:
        :param transaction_id: The ID of the original interbank transaction.
        :return: True if successful, False otherwise.
        """
        pass
