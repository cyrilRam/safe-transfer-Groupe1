from typing import List
from uuid import UUID

from bank_server.main.application.dto.user_dto import UserDto
from bank_server.main.application.interfaces.Repositories.interface_user_repository import IUserRepository
from bank_server.main.application.interfaces.Services.interface_user_service import IUserService
from bank_server.main.application.mappers.user_mapper import UserMapper


class UserService(IUserService):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def get_all_users(self) -> List[UserDto]:
        users = self.repository.get_all()
        return [UserMapper.to_dto(user) for user in users]

    def get_user_by_id(self, user_id: UUID) -> UserDto:
        user = self.repository.get_by_id(user_id)
        return UserMapper.to_dto(user)

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
