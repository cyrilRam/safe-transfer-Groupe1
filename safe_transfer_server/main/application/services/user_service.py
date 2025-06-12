from typing import List, Optional
from uuid import UUID

from safe_transfer_server.main.application.dto.user_dto import UserDto
from safe_transfer_server.main.application.interfaces.repositories.interface_user_repository import IUserRepository
from safe_transfer_server.main.application.interfaces.services.interface_user_service import IUserService
from safe_transfer_server.main.application.mappers.user_mapper import UserMapper


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def get_all_users(self) -> List[UserDto]:
        users = self.repository.get_all()
        return [UserMapper.to_dto(user) for user in users]

    def get_user_by_id(self, user_id: UUID) -> UserDto:
        user = self.repository.get_by_id(user_id)
        return UserMapper.to_dto(user)

    def get_user_by_user_bank_id(self, user_bank_id: UUID) -> Optional[UserDto]:
        user = self.repository.find_user_by_user_bank_id(user_bank_id)
        return UserMapper.to_dto(user) if user else None

    def create_user(self, user_dto: UserDto) -> UserDto:
        user = UserMapper.from_dto(user_dto)
        created_user = self.repository.create(user)
        return UserMapper.to_dto(created_user)

    def update_user(self, user_dto: UserDto) -> UserDto:
        user = UserMapper.from_dto(user_dto)
        updated_user = self.repository.update(user)
        return UserMapper.to_dto(updated_user)

    def delete_user(self, user_id: UUID) -> UserDto:
        deleted_user = self.repository.delete(user_id)
        return UserMapper.to_dto(deleted_user)

    def find_by_email_or_phone(self, email: Optional[str], phone: Optional[str]) -> Optional[UserDto]:
        user = self.repository.find_by_email_or_phone(email, phone)
        return UserMapper.to_dto(user) if user else None
