from bank_server.main.application.dto.transaction_dto import TransactionDto
from bank_server.main.application.interfaces.external_services.interface_client_safe_transfer import ISafeTransferClient


class SafeTransferClient(ISafeTransferClient):
    def execute_safe_transfer(self, dto: TransactionDto) -> None:
        # TODO
        pass
