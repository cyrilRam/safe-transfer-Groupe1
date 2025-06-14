from datetime import datetime
from typing import List
from uuid import UUID

from safe_transfer_server.main.application.dto.interbank_transaction_dto import InterbankTransactionDto, \
    InterbankTransactionCreationDto
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
from safe_transfer_server.main.application.mappers.interbank_transaction_mapper import InterbankTransactionMapper
from safe_transfer_server.main.application.utils.code_tools import CodeTools
from safe_transfer_server.main.domain.entities.transactions import InterbankTransaction
from safe_transfer_server.main.domain.enums.transactions_enums import TransactionStatus


class InterbankTransactionService(IInterbankTransactionService):

    def __init__(self, repository: IInterbankTransactionRepository, user_service: IUserService,
                 fraud_detector: IFraudDetector, mail_service: IMailService, bank_server: IBankClient):
        self.repository = repository
        self.user_service = user_service
        self.fraud_detector = fraud_detector
        self.mail_service = mail_service
        self.bank_server = bank_server

    def get_all(self) -> List[InterbankTransactionDto]:
        entities = self.repository.get_all()
        return [InterbankTransactionMapper.to_dto(e) for e in entities]

    def get_by_id(self, id: UUID) -> InterbankTransactionDto:
        entity = self.repository.get_by_id(id)
        return InterbankTransactionMapper.to_dto(entity)

    def create(self, dto: InterbankTransactionCreationDto) -> InterbankTransactionDto:
        # get the user sender
        user_sender = self.user_service.get_user_by_user_bank_id(dto.user_bank_id_source)

        # get the sender by the mail
        user_benef = self.user_service.find_by_email_or_phone(email=dto.user_dest_mail, phone=None)

        entity = InterbankTransaction(
            user_source_id=user_sender.id,
            user_dest_id=user_benef.id,
            amount=dto.amount,
            transaction_date=datetime.utcnow(),
            status=TransactionStatus.PENDING_USER,
            double_auth_source=False,
            double_auth_dest=False,
            transaction_type=dto.transaction_type,
            source_code=CodeTools.generate_code(),
            dest_code=CodeTools.generate_code()
        )
        created = self.repository.create(entity)

        self.mail_service.send_authentication_code(email=user_sender.mail, is_sender=True, code=created.source_code)
        return InterbankTransactionMapper.to_dto(created)

    def update(self, dto: InterbankTransactionDto) -> InterbankTransactionDto:
        entity = InterbankTransactionMapper.from_dto(dto)
        updated = self.repository.update(entity)
        return InterbankTransactionMapper.to_dto(updated)

    def delete(self, id: UUID) -> InterbankTransactionDto:
        deleted = self.repository.delete(id)
        return InterbankTransactionMapper.to_dto(deleted)

    def validate_sender_code(self, transaction_id: UUID, code: str) -> bool:
        transaction = self.repository.get_by_id(transaction_id)
        benef_user = self.user_service.get_user_by_id(transaction.user_dest_id)
        all_transactions_for_an_user = self.repository.get_by_sender_id(transaction.user_source_id)

        if transaction.source_code == code:
            transaction.double_auth_dest = True
            transaction.status = TransactionStatus.PENDING_FRAUD_CHECK

            if not self.fraud_detector.is_fraud(all_transactions_for_an_user, transaction):
                transaction.status = TransactionStatus.PENDING_RECIPIENT

            updated = self.repository.update(transaction)

            self.mail_service.send_authentication_code(email=benef_user.mail, is_sender=False, code=updated.dest_code)

            return True

        return False

    def validate_beneficiary_code(self, transaction_id: UUID, code: str) -> bool:
        transaction = self.repository.get_by_id(transaction_id)

        # update status
        if transaction.dest_code == code:
            transaction.status = TransactionStatus.VALIDATED
            updated = self.repository.update(transaction)

            # send update to sender
            self.bank_server.validate_sender_transaction(transaction_id)

            # send the transaction to the benef
            self.bank_server.create_beneficiary_transaction(InterbankTransactionMapper.to_dto(updated))

            return True

        return False

    def get_all_pending_transactions_for_user(self, user_id: UUID) -> List[InterbankTransactionDto]:
        transactions = self.repository.get_pending_transactions_for_user(user_id)
        pending = [t for t in transactions if
                   not t.double_auth_dest and t.status == TransactionStatus.PENDING_RECIPIENT]
        return [InterbankTransactionMapper.to_dto(t) for t in pending]

    def get_all_detected_fraud_transactions(self) -> List[InterbankTransactionDto]:
        transactions = self.repository.get_all_fraud_suspected_transactions()
        return [InterbankTransactionMapper.to_dto(t) for t in transactions]
