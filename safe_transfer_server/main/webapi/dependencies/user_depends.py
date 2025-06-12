from fastapi import Depends
from sqlalchemy.orm import Session

from safe_transfer_server.main.application.interfaces.repositories.interface_user_repository import IUserRepository
from safe_transfer_server.main.application.interfaces.services.interface_user_service import IUserService
from safe_transfer_server.main.application.services.user_service import UserService
from safe_transfer_server.main.persistance.repositories.user_repository import UserRepository
from safe_transfer_server.main.webapi.dependencies.db_depends import DbDependency


class UserDependency:
    @staticmethod
    def get_user_service(
            db: Session = Depends(DbDependency.get_db_session)
    ) -> IUserService:
        user_repo: IUserRepository = UserRepository(db)
        return UserService(user_repo)
