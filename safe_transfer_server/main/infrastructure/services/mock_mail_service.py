from safe_transfer_server.main.application.interfaces.external_services.communication_services.IMailService import \
    IMailService


class MockMailService(IMailService):
    def send_authentication_code(self, email: str, is_sender: bool, code: str) -> None:
        role = "Sender" if is_sender else "Recipient"
        # Simulate sending an email (replace with real logic in production)
        print(f"[Email to {email}]")
        print(f"Subject: Authentication Code for {role}")
        print(f"Hello {role},")
        print(f"Your authentication code is: {code}")
        print("Please enter it in the Safe Transfer system to proceed.\n")
