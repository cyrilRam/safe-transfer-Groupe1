from abc import ABC

from bank_server.main.application.interfaces.Repositories.interface_general_repository import IGeneralRepository
from bank_server.main.domain.entities.account import Account


class IAccountRepository(IGeneralRepository[Account], ABC):
    pass
