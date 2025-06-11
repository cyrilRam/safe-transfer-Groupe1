from bank_server.main.application.dto.user_dto import UserDto
from bank_server.main.domain.entities.user import User


class UserMapper:
    @staticmethod
    def to_dto(user: User) -> UserDto:
        return UserDto(
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            password=user.password,
            iban=user.iban,
            bic=user.bic,
        )

    @staticmethod
    def from_dto(dto: UserDto) -> User:
        return User(
            id=dto.id,
            name=dto.name,
            email=dto.email,
            phone=dto.phone,
            password=dto.password,
            iban=dto.iban,
            bic=dto.bic,
        )
