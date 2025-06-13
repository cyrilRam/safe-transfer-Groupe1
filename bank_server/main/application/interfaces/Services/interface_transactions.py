from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from bank_server.main.application.dto.transaction_dto import TransactionDto


class ITransactionService(ABC):
    @abstractmethod
    def get_all_transactions(self) -> List[TransactionDto]:
        pass

    @abstractmethod
    def get_all_transactions_for_account(self, account_id: UUID) -> List[TransactionDto]:
        pass

    @abstractmethod
    def get_transaction_by_id(self, transaction_id: UUID) -> TransactionDto:
        pass

    @abstractmethod
    def create_transaction(self, dto: TransactionDto, beneficiary_mail: str) -> TransactionDto:
        pass

    @abstractmethod
    def update_transaction(self, dto: TransactionDto) -> TransactionDto:
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: UUID) -> TransactionDto:
        pass

    @abstractmethod
    def validation_safe_transfer_for_sender(self, safe_transfer_id: UUID) -> TransactionDto:
        """
        update le statut de la transaction a validate et débite le montant du compte associé à la transaction
        :param safe_transfer_id:
        :return:
        """
        pass

    @abstractmethod
    def receive_validate_safe_transfer_for_beneficiary(self, dto: TransactionDto) -> TransactionDto:
        """
        cree une transaction avec le sattut validate dans le compte du benef et augmente el compte associé à la transaction
        :param dto:
        :return:
        """
