from typing import List, Annotated, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import Query

from safe_transfer_server.main.application.dto.user_dto import UserDto
from safe_transfer_server.main.application.interfaces.services.interface_user_service import IUserService
from safe_transfer_server.main.webapi.dependencies.user_depends import UserDependency

router = APIRouter(prefix="/users", tags=["Users"])
user_service_dependency = Annotated[IUserService, Depends(UserDependency.get_user_service)]


@router.get("/", response_model=List[UserDto])
def get_all_users(service: user_service_dependency):
    return service.get_all_users()


@router.get("/search", response_model=Optional[UserDto])
def search_user(
        service: user_service_dependency,
        email: Optional[str] = Query(default=None),
        phone: Optional[str] = Query(default=None),

):
    if not email and not phone:
        raise HTTPException(status_code=400, detail="Email or phone must be provided")
    user = service.find_by_email_or_phone(email=email, phone=phone)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/{user_id}", response_model=UserDto)
def get_user_by_id(user_id: UUID, service: user_service_dependency):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserDto, status_code=status.HTTP_201_CREATED)
def create_user(user_dto: UserDto, service: user_service_dependency):
    return service.create_user(user_dto)


@router.put("/", response_model=UserDto)
def update_user(user_dto: UserDto, service: user_service_dependency):
    return service.update_user(user_dto)


@router.delete("/{user_id}", response_model=UserDto)
def delete_user(user_id: UUID, service: user_service_dependency):
    return service.delete_user(user_id)
