class Twilio:
    def __init__(self):
        from twilio.rest import Client
        from utils.parcer import account_token, account_sid
        self.account_sid = account_sid
        self.auth_token = account_token
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, msg: str) -> None:
          from utils.parcer import twilio_phone_number, to_phone_number
          message = self.client.messages.create(
          from_ = twilio_phone_number,
          body = msg,
          to = to_phone_number
        )

          print("Message sent successfully. ID: {message.sid}")