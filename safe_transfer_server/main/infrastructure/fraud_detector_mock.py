from typing import List

from safe_transfer_server.main.application.interfaces.external_services.ia_services import IFraudDetector
from safe_transfer_server.main.domain.entities.transactions import InterbankTransaction


class MockFraudDetector(IFraudDetector):
    def is_fraud(self, all_transactions: List[InterbankTransaction],
                 transaction_to_check: InterbankTransaction) -> bool:
        return False
