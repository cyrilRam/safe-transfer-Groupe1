from enum import Enum


class TransactionStatus(str, Enum):
    PENDING_USER = "PENDING_USER"
    PENDING_FRAUD_CHECK = "PENDING_FRAUD_CHECK"
    PENDING_RECIPIENT = "PENDING_RECIPIENT"
    VALIDATED = "VALIDATED"
    REFUSED = "REFUSED"


class TransactionType(str, Enum):
    TRANSFER = "TRANSFER"
    WITHDRAWAL = "WITHDRAWAL"
