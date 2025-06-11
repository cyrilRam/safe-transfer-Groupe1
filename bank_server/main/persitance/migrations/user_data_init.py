import uuid

from bank_server.main.domain.entities.user import User
from bank_server.main.persitance.config.database_connection import DataBaseConnection


def seed_users():
    db = DataBaseConnection()
    session = db.local_session_creation()

    if session.query(User).first():
        print("Des utilisateurs existent déjà. Aucune insertion effectuée.")
        session.close()
        return

    users = [
        User(
            id=uuid.UUID("11111111-1111-1111-1111-111111111111"),
            name="Alice Dupont",
            email="alice.dupont@example.com",
            phone="+33612345678",
            password="hashed_password_1",
            iban="FR7630006000011234567890189",
            bic="AGRIFRPP"
        ),
        User(
            id=uuid.UUID("22222222-2222-2222-2222-222222222222"),
            name="Bob Martin",
            email="bob.martin@example.com",
            phone="+33687654321",
            password="hashed_password_2",
            iban="FR1420041010050500013M02606",
            bic="BNPAFRPP"
        ),
        User(
            id=uuid.UUID("33333333-3333-3333-3333-333333333333"),
            name="Claire Moreau",
            email="claire.moreau@example.com",
            phone="+33699887766",
            password="hashed_password_3",
            iban="FR7630007000110009970004942",
            bic="CCFRFRPP"
        )
    ]

    session.add_all(users)
    session.commit()
    session.close()
    print("Utilisateurs insérés avec succès.")


if __name__ == "__main__":
    seed_users()
