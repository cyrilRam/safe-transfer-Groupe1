from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from safe_transfer_server.main.application.interfaces.repositories.interface_general_repository import \
    IGeneralRepository
from safe_transfer_server.main.domain.entities.user import User


class IUserRepository(IGeneralRepository[User], ABC):
    @abstractmethod
    def find_by_email_or_phone(self, email: Optional[str], phone: Optional[str]) -> Optional[User]:
        pass

    @abstractmethod
    def find_user_by_user_bank_id(self, user_bank_id: UUID) -> Optional[User]:
        pass
