from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from bank_server.main.application.dto.user_dto import UserDto


class IUserService(ABC):
    @abstractmethod
    def get_all_users(self) -> List[UserDto]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: UUID) -> UserDto:
        pass

    @abstractmethod
    def create_user(self, user_dto: UserDto) -> UserDto:
        pass

    @abstractmethod
    def update_user(self, user_dto: UserDto) -> UserDto:
        pass

    @abstractmethod
    def delete_user(self, user_id: UUID) -> UserDto:
        pass
