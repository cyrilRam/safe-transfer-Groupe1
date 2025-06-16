# safe_transfer_server/main/application/mappers/interaction_chat_ia_mapper.py

from typing import List, Dict
from safe_transfer_server.main.application.dto.interaction_ia_dto import SessionInteractionDto


class InteractionChatIaMapper:

    @staticmethod
    def to_cohere_chat_history(session: SessionInteractionDto) -> List[Dict[str, str]]:
        """
        Transforme une session d'interactions en historique au format compatible Cohere Chat API.
        Chaque interaction génère deux messages : un de l'utilisateur et un du chatbot.
        """
        messages = []

        for interaction in session.interactions:
            messages.append({"role": "user", "message": interaction.prompt})
            messages.append({"role": "chatbot", "message": interaction.response})

        return messages
