from config import config
import requests
from twilio.rest import Client

class WhatsAppAdapter():
    # def __init__(self, algo):
    #     self.algo = algo
    def send_message(self, to, messageBody):
        client = Client(config["ACCOUNT_SID"], config["AUTH_TOKEN"])
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            to=f"whatsapp:{to}",
            body=messageBody
        )


        # url = f"https://graph.facebook.com/{config['VERSION']}/{config['PHONE_NUMBER_ID']}/messages"
        # headers = {
        #     "Authorization": f"Bearer {config['ACCESS_TOKEN']}",
        #     "Content-Type": "application/json"
        # }

        # data = {
        #     "messaging_product": "whatsapp",
        #     "to": "+50683962643",
        #     "type": "text",
        #     "body": message
        # }

        # response = requests.post(url, headers=headers, json=data)
        # return response