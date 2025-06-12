from abc import ABC, abstractmethod


class IMailService(ABC):
    @abstractmethod
    def send_authentication_code(self, email: str, is_sender: bool, code: str) -> None:
        """
        Sends an authentication code to a given email address.

        :param email: The recipient's email address.
        :param is_sender: True if the recipient is the sender, False if it's the recipient.
        :param code: The authentication code to send.
        """
        pass
