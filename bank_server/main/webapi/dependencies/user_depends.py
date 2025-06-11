from fastapi import Depends
from sqlalchemy.orm import Session

from bank_server.main.application.interfaces.Repositories.interface_user_repository import IUserRepository
from bank_server.main.application.interfaces.Services.interface_user_service import IUserService
from bank_server.main.application.services.user_service import UserService
from bank_server.main.persitance.repositories.user_repository import UserRepository
from bank_server.main.webapi.dependencies.db_depends import DbDependency


class UserDependency:
    @staticmethod
    def get_user_service(
            db: Session = Depends(DbDependency.get_db_session)
    ) -> IUserService:
        user_repo: IUserRepository = UserRepository(db)
        return UserService(user_repo)
