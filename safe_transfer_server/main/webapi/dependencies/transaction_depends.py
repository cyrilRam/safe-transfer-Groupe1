from fastapi import Depends
from sqlalchemy.orm import Session

from safe_transfer_server.main.application.interfaces.external_services.bank_client.interface_bank_client import \
    IBankClient
from safe_transfer_server.main.application.interfaces.external_services.communication_services.IMailService import \
    IMailService
from safe_transfer_server.main.application.interfaces.external_services.ia_services.interface_fraude_detector import \
    IFraudDetector
from safe_transfer_server.main.application.interfaces.repositories.interface_transaction_repository import \
    IInterbankTransactionRepository
from safe_transfer_server.main.application.interfaces.services.interface_transaction_service import \
    IInterbankTransactionService
from safe_transfer_server.main.application.interfaces.services.interface_user_service import IUserService
from safe_transfer_server.main.application.services.interbank_transaction_service import InterbankTransactionService
from safe_transfer_server.main.infrastructure.services.bank_client_http import BankHttpClient
from safe_transfer_server.main.infrastructure.services.fraud_detector_mock import MockFraudDetector
from safe_transfer_server.main.infrastructure.services.mock_mail_service import MockMailService
from safe_transfer_server.main.persistance.repositories.interbank_transaction_repository import \
    InterbankTransactionRepository
from safe_transfer_server.main.webapi.dependencies.db_depends import DbDependency
from safe_transfer_server.main.webapi.dependencies.user_depends import UserDependency


class InterbankTransactionDependency:
    @staticmethod
    def get_transaction_service(
            db: Session = Depends(DbDependency.get_db_session),
            user_service: IUserService = Depends(UserDependency.get_user_service)
    ) -> IInterbankTransactionService:
        # Instanciate all other dependencies here
        repo: IInterbankTransactionRepository = InterbankTransactionRepository(db)
        fraud_detector: IFraudDetector = MockFraudDetector()
        mail_service: IMailService = MockMailService()
        bank_client: IBankClient = BankHttpClient()

        return InterbankTransactionService(
            repository=repo,
            user_service=user_service,
            fraud_detector=fraud_detector,
            mail_service=mail_service,
            bank_server=bank_client
        )
