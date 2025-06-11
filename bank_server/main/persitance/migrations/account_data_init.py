from datetime import datetime
from uuid import UUID

from bank_server.main.domain.entities.account import Account
from bank_server.main.domain.entities.user import User
from bank_server.main.persitance.config.database_connection import DataBaseConnection

FIXED_ACCOUNTS = {
    "11111111-1111-1111-1111-111111111111": "aaaaaaa1-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
    "22222222-2222-2222-2222-222222222222": "bbbbbbb2-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
    "33333333-3333-3333-3333-333333333333": "ccccccc3-cccc-cccc-cccc-cccccccccccc",
}


def seed_accounts():
    db = DataBaseConnection()
    session = db.local_session_creation()

    users = session.query(User).all()

    if not users:
        print("Aucun utilisateur trouvé. Veuillez exécuter seed_users.py d'abord.")
        session.close()
        return

    existing_accounts = session.query(Account).first()
    if existing_accounts:
        print("Des comptes existent déjà. Aucune insertion effectuée.")
        session.close()
        return
    accounts = []
    for user in users:
        account_id = UUID(FIXED_ACCOUNTS[str(user.id)])
        account = Account(
            id=account_id,
            user_id=user.id,
            balance=1000.0,
            opening_date=datetime.utcnow(),
            name=f"Compte de {user.name}"
        )
        accounts.append(account)

    session.add_all(accounts)
    session.commit()
    session.close()
    print("Comptes créés avec succès avec des UUID fixes.")


if __name__ == "__main__":
    seed_accounts()
