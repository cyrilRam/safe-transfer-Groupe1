from typing import List

from safe_transfer_server.main.application.dto.interaction_ia_dto import InteractionDto, SessionInteractionDto
from safe_transfer_server.main.domain.entities.chat_ia import InteractionIa


class InteractionChatIaMapper:
    @staticmethod
    def to_dto(entity: InteractionIa) -> InteractionDto:
        return InteractionDto(
            id=entity.id,
            session_id=entity.session_id,
            prompt=entity.prompt,
            response=entity.response,
            created_at=entity.created_at
        )

    @staticmethod
    def from_dto(dto: InteractionDto) -> InteractionIa:
        return InteractionIa(
            id=dto.id,
            session_id=dto.session_id,
            prompt=dto.prompt,
            response=dto.response,
            created_at=dto.created_at
        )

    @staticmethod
    def to_session_dto(session_id, interactions: List[InteractionIa]) -> SessionInteractionDto:
        return SessionInteractionDto(
            session_id=session_id,
            interactions=[InteractionChatIaMapper.to_dto(i) for i in interactions]
        )
