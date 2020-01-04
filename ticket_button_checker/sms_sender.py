from twilio.rest import Client

import settings


class SMSSender:
    def __init__(self):
        self.phone = settings.PHONE
        self.client = Client(settings.Twilio.SID, settings.Twilio.TOKEN)

    def send_sms(self):
        self.client.messages.create(to=settings.PHONE,
                                    from_=settings.Twilio.PHONE,
                                    body=settings.SMS_TEXT)
