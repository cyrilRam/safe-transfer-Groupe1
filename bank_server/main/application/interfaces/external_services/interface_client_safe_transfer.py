from uuid import UUID


class ISafeTransferClient:
    def execute_safe_transfer(self, amount: float, user_id: UUID, beneficiary_mail: str) -> UUID:
        pass
