from typing import Optional
import cohere

from safe_transfer_server.main.application.dto.interaction_ia_dto import SessionInteractionDto, RequestChatDto, \
    InteractionDto
from safe_transfer_server.main.application.interfaces.external_services.ia_services.interface_chat_generator import \
    IIaChatGenerator
from safe_transfer_server.main.infrastructure.mappers.interaction_chat_ia_mapper import InteractionChatIaMapper
from safe_transfer_server.main.infrastructure.services.ia.prompts.cohere_safe_transfer_prompt import \
    SAFE_TRANSFER_CONTEXT_PROMPT


class IaCohereService(IIaChatGenerator):
    def __init__(self, cohere_api_key: str):
        self.client = cohere.Client(cohere_api_key)
    def generate_interaction_ia(self, chat_history: Optional[SessionInteractionDto],
                                request: RequestChatDto) -> InteractionDto:
        # Récupération des anciens messages au format Cohere Chat API
        history_messages = (
            InteractionChatIaMapper.to_cohere_chat_history(chat_history)
            if chat_history else []
        )

        # Ajout de la question actuelle
        full_messages = history_messages + [{"role": "user", "message": request.prompt}]

        try:
            response = self.client.chat(
                model="command-r-plus",
                message=request.prompt,
                chat_history=history_messages,
                prompt_truncation="auto",
                temperature=0.5,
                connectors=[],
                preamble=SAFE_TRANSFER_CONTEXT_PROMPT.strip()
            )

            generated_text = response.text.strip()

        except Exception as e:
            generated_text = f"Erreur lors de la génération de la réponse : {str(e)}"

        return InteractionDto(
            prompt=request.prompt,
            response=generated_text
        )