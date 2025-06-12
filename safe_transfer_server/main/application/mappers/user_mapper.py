from safe_transfer_server.main.application.dto.user_dto import UserDto
from safe_transfer_server.main.domain.entities.user import User


class UserMapper:
    @staticmethod
    def to_dto(user: User) -> UserDto:
        return UserDto(
            id=user.id,
            id_bank_user=user.id_bank_user,
            name=user.name,
            mail=user.mail,
            phone=user.phone,
            account_id=user.account_id
        )

    @staticmethod
    def from_dto(dto: UserDto) -> User:
        return User(
            id=dto.id,
            id_bank_user=dto.id_bank_user,
            name=dto.name,
            mail=dto.mail,
            phone=dto.phone,
            account_id=dto.account_id
        )
