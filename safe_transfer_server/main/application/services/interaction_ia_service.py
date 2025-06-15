from datetime import datetime
from uuid import UUID, uuid4

from safe_transfer_server.main.application.dto.interaction_ia_dto import SessionInteractionDto, RequestChatDto, \
    InteractionDto
from safe_transfer_server.main.application.interfaces.external_services.ia_services.interface_chat_generator import \
    IIaChatGenerator
from safe_transfer_server.main.application.interfaces.repositories.interface_interactions_ia import \
    IInteractionRepository
from safe_transfer_server.main.application.interfaces.services.interface_chat_ia_service import \
    IInteractionChatIaService
from safe_transfer_server.main.application.mappers.interaction_ia_mapper import InteractionChatIaMapper


class InteractionChatIaService(IInteractionChatIaService):

    def __init__(self, repository: IInteractionRepository, chat_ia_service: IIaChatGenerator):
        self.repository = repository
        self.chat_ia_service = chat_ia_service

    def process_interactions(self, request: RequestChatDto) -> SessionInteractionDto:
        chat_history = []

        # Step 1: If a session_id is provided, retrieve all past interactions
        if request.session_id is not None:
            entities = self.repository.get_all_by_session_id(request.session_id)
            chat_history = InteractionChatIaMapper.to_session_dto(request.session_id, entities)

        # Step 2: Generate the new interaction using the AI service
        interaction: InteractionDto = self.chat_ia_service.generate_interaction_ia(chat_history, request)

        # Step 3: If no session_id was provided, generate a new one (new session)
        if request.session_id is None:
            request.session_id = uuid4()

        # Step 4: Map the generated interaction to an entity and persist it in the database
        new_entity = InteractionChatIaMapper.from_dto(InteractionDto(
            id=uuid4(),
            session_id=request.session_id,
            prompt=interaction.prompt,
            response=interaction.response,
            created_at=datetime.utcnow()
        ))
        self.repository.create(new_entity)

        # Step 5: Retrieve the updated list of interactions and return as session DTO
        updated_entities = self.repository.get_all_by_session_id(request.session_id)
        return InteractionChatIaMapper.to_session_dto(request.session_id, updated_entities)

    def get_interactions_by_session_id(self, session_id: UUID) -> SessionInteractionDto:
        entities = self.repository.get_all_by_session_id(session_id)
        return InteractionChatIaMapper.to_session_dto(session_id, entities)
