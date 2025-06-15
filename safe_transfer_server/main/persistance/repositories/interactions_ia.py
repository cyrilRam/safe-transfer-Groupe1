from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session

from safe_transfer_server.main.application.interfaces.repositories.interface_interactions_ia import \
    IInteractionRepository
from safe_transfer_server.main.domain.entities.chat_ia import InteractionIa
from safe_transfer_server.main.persistance.repositories.general_repository import GeneralRepository


class InteractionRepository(GeneralRepository[InteractionIa], IInteractionRepository):
    def __init__(self, session: Session):
        self.session = session
        super().__init__(session=session, model=InteractionIa)

    def get_all_by_session_id(self, session_id: UUID) -> list[Type[InteractionIa]]:
        """
        Returns all interactions for a specific session.
        """
        return self.session.query(InteractionIa).filter(InteractionIa.session_id == session_id).all()
