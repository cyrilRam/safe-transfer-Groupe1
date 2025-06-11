from sqlalchemy.orm import Session

from bank_server.main.application.interfaces.Repositories.interface_user_repository import IUserRepository
from bank_server.main.domain.entities.user import User
from bank_server.main.persitance.repositories.general_repository import GeneralRepository


class UserRepository(GeneralRepository[User], IUserRepository):
    def __init__(self, session: Session):
        self.session = session
        super().__init__(session=session, model=User)
