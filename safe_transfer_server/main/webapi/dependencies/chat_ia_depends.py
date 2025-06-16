
from fastapi import Depends
from sqlalchemy.orm import Session
import os
from safe_transfer_server.main.application.interfaces.external_services.ia_services.interface_chat_generator import IIaChatGenerator
from safe_transfer_server.main.application.interfaces.repositories.interface_interactions_ia import IInteractionRepository
from safe_transfer_server.main.application.interfaces.services.interface_chat_ia_service import IInteractionChatIaService
from safe_transfer_server.main.application.services.interaction_ia_service import InteractionChatIaService
from safe_transfer_server.main.infrastructure.services.ia.chat_ia_cohere_service import IaCohereService
from safe_transfer_server.main.persistance.repositories.interactions_ia import InteractionRepository
from safe_transfer_server.main.webapi.dependencies.db_depends import DbDependency


class ChatIaDependency:
    @staticmethod
    def get_ia_chat_service(
        db: Session = Depends(DbDependency.get_db_session)
    ) -> IInteractionChatIaService:
        repository: IInteractionRepository = InteractionRepository(db)
        ia_generator: IIaChatGenerator = IaCohereService(cohere_api_key=os.getenv("COHERE_API_KEY"))

        return InteractionChatIaService(
            repository=repository,
            chat_ia_service=ia_generator
        )