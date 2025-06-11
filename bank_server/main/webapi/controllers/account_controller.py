from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from bank_server.main.application.dto.account_dto import AccountDto
from bank_server.main.application.interfaces.Services.interafce_account_service import IAccountService
from bank_server.main.webapi.dependencies.account_dependency import AccountDependency

router = APIRouter(prefix="/accounts", tags=["Accounts"])
account_service_dependency = Annotated[IAccountService, Depends(AccountDependency.get_account_service)]


@router.get("/", response_model=List[AccountDto])
def get_all_accounts(service: account_service_dependency):
    return service.get_all_accounts()


@router.get("/{account_id}", response_model=AccountDto)
def get_account_by_id(account_id: UUID, service: account_service_dependency):
    account = service.get_account_by_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@router.post("/", response_model=AccountDto, status_code=status.HTTP_201_CREATED)
def create_account(dto: AccountDto, service: account_service_dependency):
    return service.create_account(dto)


@router.put("/", response_model=AccountDto)
def update_account(dto: AccountDto, service: account_service_dependency):
    return service.update_account(dto)


@router.delete("/{account_id}", response_model=AccountDto)
def delete_account(account_id: UUID, service: account_service_dependency):
    return service.delete_account(account_id)
