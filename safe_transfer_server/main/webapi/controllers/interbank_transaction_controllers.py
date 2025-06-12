from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from safe_transfer_server.main.application.dto.interbank_transaction_dto import InterbankTransactionDto, \
    InterbankTransactionCreationDto
from safe_transfer_server.main.application.interfaces.services.interface_transaction_service import \
    IInterbankTransactionService
from safe_transfer_server.main.webapi.dependencies.transaction_depends import InterbankTransactionDependency

router = APIRouter(prefix="/transactions", tags=["Interbank Transactions"])
transaction_service_dependency = Annotated[
    IInterbankTransactionService, Depends(InterbankTransactionDependency.get_transaction_service)]


@router.get("/", response_model=List[InterbankTransactionDto])
def get_all_transactions(service: transaction_service_dependency):
    return service.get_all()


@router.get("/{transaction_id}", response_model=InterbankTransactionDto)
def get_transaction_by_id(transaction_id: UUID, service: transaction_service_dependency):
    transaction = service.get_by_id(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.post("/", response_model=InterbankTransactionDto, status_code=status.HTTP_201_CREATED)
def create_transaction(dto: InterbankTransactionCreationDto, service: transaction_service_dependency):
    return service.create(dto)


@router.put("/", response_model=InterbankTransactionDto)
def update_transaction(dto: InterbankTransactionDto, service: transaction_service_dependency):
    return service.update(dto)


@router.delete("/{transaction_id}", response_model=InterbankTransactionDto)
def delete_transaction(transaction_id: UUID, service: transaction_service_dependency):
    return service.delete(transaction_id)
