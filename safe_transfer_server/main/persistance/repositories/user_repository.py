from typing import Optional
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session

from safe_transfer_server.main.application.interfaces.repositories.interface_user_repository import IUserRepository
from safe_transfer_server.main.domain.entities.user import User
from safe_transfer_server.main.persistance.repositories.general_repository import GeneralRepository


class UserRepository(GeneralRepository[User], IUserRepository):
    def __init__(self, session: Session):
        self.session = session
        super().__init__(session=session, model=User)

    def find_by_email_or_phone(self, email: Optional[str], phone: Optional[str]) -> Optional[User]:
        query = self.session.query(User)
        if email and phone:
            return query.filter(or_(User.mail == email, User.phone == phone)).first()
        elif email:
            return query.filter(User.mail == email).first()
        elif phone:
            return query.filter(User.phone == phone).first()
        return None

    def find_user_by_user_bank_id(self, user_bank_id: UUID) -> Optional[User]:
        return self.session.query(User).filter(User.id_bank_user == user_bank_id).first()
