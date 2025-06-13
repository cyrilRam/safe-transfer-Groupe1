from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from bank_server.main.application.dto.transaction_dto import TransactionDto
from bank_server.main.application.interfaces.Services.interface_transactions import ITransactionService
from bank_server.main.webapi.dependencies.TransactionDependency import TransactionDependency

router = APIRouter(prefix="/transactions", tags=["Transactions"])
transaction_service_dependency = Annotated[ITransactionService, Depends(TransactionDependency.get_transaction_service)]


@router.get("/", response_model=List[TransactionDto])
def get_all_transactions(service: transaction_service_dependency):
    return service.get_all_transactions()


@router.get("/{transaction_id}", response_model=TransactionDto)
def get_transaction(transaction_id: UUID, service: transaction_service_dependency):
    return service.get_transaction_by_id(transaction_id)


@router.post("/", response_model=TransactionDto)
def create_transaction(dto: TransactionDto, beneficiary_mail: str, service: transaction_service_dependency):
    return service.create_transaction(dto, beneficiary_mail)


@router.put("/", response_model=TransactionDto)
def update_transaction(dto: TransactionDto, service: transaction_service_dependency):
    return service.update_transaction(dto)


@router.delete("/{transaction_id}", response_model=TransactionDto)
def delete_transaction(transaction_id: UUID, service: transaction_service_dependency):
    return service.delete_transaction(transaction_id)


@router.get("/by-account/{account_id}", response_model=List[TransactionDto])
def get_transactions_by_account(account_id: UUID, service: transaction_service_dependency):
    return service.get_all_transactions_for_account(account_id)


@router.put("/{transaction_id}/safe-transfer/validation-sender", response_model=TransactionDto)
def validation_safe_transfer_for_sender(transaction_id: UUID, service: transaction_service_dependency):
    return service.validation_safe_transfer_for_sender(transaction_id)


@router.post("/safe-transfer/creation-beneficiary", response_model=TransactionDto)
def receive_validate_safe_transfer_for_beneficiary(dto: TransactionDto, service: transaction_service_dependency):
    return service.receive_validate_safe_transfer_for_beneficiary(dto)
