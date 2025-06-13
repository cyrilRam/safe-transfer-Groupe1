from typing import List
from uuid import UUID

from bank_server.main.application.Exceptions.general_exceptions import SafeTransferException, ObjectNotFoundException
from bank_server.main.application.dto.transaction_dto import TransactionDto
from bank_server.main.application.interfaces.Repositories.interface_transaction_repository import ITransactionRepository
from bank_server.main.application.interfaces.Services.interafce_account_service import IAccountService
from bank_server.main.application.interfaces.Services.interface_transactions import ITransactionService
from bank_server.main.application.interfaces.external_services.interface_client_safe_transfer import ISafeTransferClient
from bank_server.main.application.mappers.transaction_mapper import TransactionMapper
from bank_server.main.domain.enums.transaction_enums import TransactionStatus


class TransactionService(ITransactionService):

    def __init__(self, repository: ITransactionRepository, client_safe_transfer: ISafeTransferClient,
                 account_service: IAccountService):
        self.repository = repository
        self.client_safe_transfer = client_safe_transfer
        self.account_service = account_service

    def get_all_transactions(self) -> List[TransactionDto]:
        return [TransactionMapper.to_dto(t) for t in self.repository.get_all()]

    def get_all_transactions_for_account(self, account_id: UUID) -> List[TransactionDto]:
        transactions = self.repository.get_all_by_account_id(account_id)
        return [TransactionMapper.to_dto(tx) for tx in transactions]

    def get_transaction_by_id(self, transaction_id: UUID) -> TransactionDto:
        return TransactionMapper.to_dto(self.repository.get_by_id(transaction_id))

    def create_transaction(self, dto: TransactionDto, beneficiary_mail: str) -> TransactionDto:
        account_sender = self.account_service.get_account_by_id(dto.account_id)
        safe_transfer_id_trans = None
        if dto.transaction_type == "SAFETRANSFER_VIREMENT":
            try:
                safe_transfer_id_trans = self.client_safe_transfer.execute_safe_transfer(dto.amount,
                                                                                         account_sender.user_id,
                                                                                         beneficiary_mail)
            except Exception as e:
                raise SafeTransferException(type(dto), str(e))

        return TransactionMapper.to_dto(self.repository.create(TransactionMapper.from_dto(dto)))

    def update_transaction(self, dto: TransactionDto) -> TransactionDto:
        return TransactionMapper.to_dto(self.repository.update(TransactionMapper.from_dto(dto)))

    def delete_transaction(self, transaction_id: UUID) -> TransactionDto:
        return TransactionMapper.to_dto(self.repository.delete(transaction_id))

    def validation_safe_transfer_for_sender(self, safe_transfer_id: UUID) -> TransactionDto:
        # check if the transaction exists
        existing_transaction = self.repository.get_by_safe_transfer_id(safe_transfer_id)
        if not existing_transaction:
            raise ObjectNotFoundException(object_type=TransactionDto,
                                          id_object=str(existing_transaction.transaction_id))

        # update statut transaction
        existing_transaction.status = TransactionStatus.VALIDATED.value
        self.repository.update(existing_transaction)

        # debite account
        account = self.account_service.get_account_by_id(existing_transaction.account_id)
        account.balance = account.balance - existing_transaction.amount
        self.account_service.update_account(account)

        return TransactionMapper.to_dto(existing_transaction)

    def receive_validate_safe_transfer_for_beneficiary(self, dto: TransactionDto) -> TransactionDto:
        # create the transaction
        dto.status = TransactionStatus.VALIDATED.value
        created_transaction = self.create_transaction(dto)

        # update account amount
        account = self.account_service.get_account_by_id(dto.account_id)
        account.balance = account.balance + dto.amount
        self.account_service.update_account(account)

        return created_transaction
