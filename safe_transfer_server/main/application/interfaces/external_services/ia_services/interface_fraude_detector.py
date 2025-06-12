from abc import ABC, abstractmethod
from typing import List

from safe_transfer_server.main.domain.entities.transactions import InterbankTransaction


class IFraudDetector(ABC):
    @abstractmethod
    def is_fraud(self, all_transactions: List[InterbankTransaction],
                 transaction_to_check: InterbankTransaction) -> bool:
        """
        Determines whether a transaction is fraudulent based on historical data.

        :param all_transactions: List of all existing interbank transactions.
        :param transaction_to_check: The transaction to evaluate.
        :return: True if the transaction is considered fraudulent, False otherwise.
        """
        pass
