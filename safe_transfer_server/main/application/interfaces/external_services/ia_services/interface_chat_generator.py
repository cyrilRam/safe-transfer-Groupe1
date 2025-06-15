from abc import ABC, abstractmethod
from typing import Optional

from safe_transfer_server.main.application.dto.interaction_ia_dto import SessionInteractionDto, InteractionDto, \
    RequestChatDto


class IIaChatGenerator(ABC):
    @abstractmethod
    def generate_interaction_ia(self, chat_history: Optional[SessionInteractionDto],
                                request: RequestChatDto) -> InteractionDto:
        pass
