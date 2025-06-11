from datetime import datetime
from uuid import UUID

import bank_server.main.domain.entities.account  # noqa: F401
import bank_server.main.domain.entities.transaction  # noqa: F401
# Pour forcer le chargement des tables référencées
import bank_server.main.domain.entities.user  # noqa: F401
from bank_server.main.domain.entities.transaction import Transaction
from bank_server.main.domain.enums.transaction_enums import TransactionStatus, TransactionType
from bank_server.main.persitance.config.database_connection import DataBaseConnection


def seed_transactions():
    db = DataBaseConnection()
    session = db.local_session_creation()

    existing = session.query(Transaction).first()
    if existing:
        print("Des transactions existent déjà. Aucune insertion.")
        session.close()
        return

    transactions = [
        Transaction(
            transaction_id=UUID("ddddddd1-dddd-dddd-dddd-dddddddddddd"),
            account_id=UUID("aaaaaaa1-aaaa-aaaa-aaaa-aaaaaaaaaaaa"),  # Alice
            amount=250.0,
            transaction_date=datetime.utcnow(),
            status=TransactionStatus.VALIDATED,
            fraud_detected=False,
            transaction_type=TransactionType.CLASSIC_VIREMENT,
            counterparty_name="Bob Martin"
        ),
        Transaction(
            transaction_id=UUID("eeeeeee2-eeee-eeee-eeee-eeeeeeeeeeee"),
            account_id=UUID("bbbbbbb2-bbbb-bbbb-bbbb-bbbbbbbbbbbb"),  # Bob
            amount=400.0,
            transaction_date=datetime.utcnow(),
            status=TransactionStatus.VALIDATED,
            fraud_detected=False,
            transaction_type=TransactionType.CLASSIC_VIREMENT,
            counterparty_name="Claire Moreau"
        )
    ]

    session.add_all(transactions)
    session.commit()
    session.close()
    print("Transactions avec contrepartie insérées avec succès.")


if __name__ == "__main__":
    seed_transactions()
