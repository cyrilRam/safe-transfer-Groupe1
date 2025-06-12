import uuid
from datetime import datetime

from safe_transfer_server.main.domain.entities.transactions import InterbankTransaction
from safe_transfer_server.main.domain.entities.user import User
from safe_transfer_server.main.domain.enums.transactions_enums import TransactionStatus, TransactionType
from safe_transfer_server.main.persistance.config.database_connection import DataBaseConnection


def seed_valid_transaction():
    db = DataBaseConnection()
    session = db.local_session_creation()

    # Vérifie si une transaction existe déjà
    if session.query(InterbankTransaction).first():
        print("Une transaction existe déjà. Aucune insertion effectuée.")
        session.close()
        return
    user = User()
    transaction = InterbankTransaction(
        id=uuid.uuid4(),
        user_source_id=uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"),  # Alice
        user_dest_id=uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"),  # Bob
        amount=250.0,
        status=TransactionStatus.VALIDATED,
        transaction_date=datetime.utcnow(),
        double_auth_source=True,
        double_auth_dest=True,
        transaction_type=TransactionType.TRANSFER,
        source_code="SRC123",
        dest_code="DST456"
    )

    session.add(transaction)
    session.commit()
    session.close()
    print("Transaction validée insérée avec succès.")


if __name__ == "__main__":
    seed_valid_transaction()
