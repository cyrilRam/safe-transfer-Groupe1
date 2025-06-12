import uuid

from safe_transfer_server.main.domain.entities.user import User
from safe_transfer_server.main.persistance.config.database_connection import DataBaseConnection


def seed_safe_transfer_users():
    db = DataBaseConnection()
    session = db.local_session_creation()

    if session.query(User).first():
        print("Des utilisateurs existent déjà dans le système Safe Transfer. Aucune insertion effectuée.")
        session.close()
        return

    users = [
        User(
            id=uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"),
            id_bank_user=uuid.UUID("11111111-1111-1111-1111-111111111111"),
            name="Alice Dupont",
            mail="alice.dupont@example.com",
            phone="+33612345678",
            account_id=uuid.UUID("aaaaaaa1-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
        ),
        User(
            id=uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"),
            id_bank_user=uuid.UUID("22222222-2222-2222-2222-222222222222"),
            name="Bob Martin",
            mail="bob.martin@example.com",
            phone="+33687654321",
            account_id=uuid.UUID("bbbbbbb2-bbbb-bbbb-bbbb-bbbbbbbbbbbb")
        ),
        User(
            id=uuid.UUID("cccccccc-cccc-cccc-cccc-cccccccccccc"),
            id_bank_user=uuid.UUID("33333333-3333-3333-3333-333333333333"),
            name="Claire Moreau",
            mail="claire.moreau@example.com",
            phone="+33699887766",
            account_id=uuid.UUID("ccccccc3-cccc-cccc-cccc-cccccccccccc")
        )
    ]

    session.add_all(users)
    session.commit()
    session.close()
    print("Utilisateurs Safe Transfer insérés avec succès avec UUID fixes.")


if __name__ == "__main__":
    seed_safe_transfer_users()
