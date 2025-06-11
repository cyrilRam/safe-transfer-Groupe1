from bank_server.main.application.dto.transaction_dto import TransactionDto


class ISafeTransferClient:
    def execute_safe_transfer(self, dto: TransactionDto) -> None:
        pass
