from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from safe_transfer_server.main.application.dto.interbank_transaction_dto import InterbankTransactionDto, \
    InterbankTransactionCreationDto


class IInterbankTransactionService(ABC):
    @abstractmethod
    def get_all(self) -> List[InterbankTransactionDto]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> InterbankTransactionDto:
        pass

    @abstractmethod
    def get_all_pending_transactions_for_user(self, user_id: UUID) -> InterbankTransactionDto:
        pass

    @abstractmethod
    def get_all_detected_fraud_transactions(self, user_id: UUID) -> InterbankTransactionDto:
        pass

    @abstractmethod
    def create(self, dto: InterbankTransactionCreationDto) -> InterbankTransactionDto:
        pass

    @abstractmethod
    def update(self, dto: InterbankTransactionDto) -> InterbankTransactionDto:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> InterbankTransactionDto:
        pass

    @abstractmethod
    def validate_sender_code(self, transaction_id: UUID, code: str) -> bool:
        """
        Validates the sender's authentication code for a given transaction.

        - If the code matches, the transaction's `double_auth_source` is confirmed.
        - Triggers a fraud detection check using the user's transaction history.
        - If no fraud is detected, updates the transaction status to PENDING_RECIPIENT.
        - If fraud is suspected, status remains PENDING_FRAUD_CHECK.

        :param transaction_id: The unique ID of the transaction to validate.
        :param code: The sender's authentication code to validate.
        :return: True if validation is successful (code is correct), False otherwise.
        """
        pass

    def validate_beneficiary_code(self, transaction_id: UUID, code: str) -> bool:
        """
        check code benef
        passe la transact en validate
        appelle /api/safe-transfer/transactions/{id}/validate (valide la transaction du sender chez sa banque + debite compte)
        appelle /api/safe-transfert/beneficiary-transaction (cree la transact chez le benef et credite le compte)
        :param transaction_id:
        :param code:
        :return:
        """
        pass
