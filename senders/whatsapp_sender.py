from config import config
from typing import Dict
import logging
from twilio.rest import Client
logger = logging.getLogger(__name__)



def send_whatsapp(to: str, message_body: str) -> Dict[str, str]:
    try:
        account_sid = config["ACCOUNT_SID"]
        auth_token = config["AUTH_TOKEN"]
        if not account_sid or not auth_token:
            logger.error("Twilio credentials not configured properly")
            raise ValueError("Missing Twilio configuration")
        
        client = Client(account_sid, auth_token)




        message = client.messages.create(
            from_="whatsapp:+14155238886",
            to=to,
            body=message_body
        )
        return {"sid": message.sid, "status": message.status}
    except Exception as e:
        logger.error(f"Failed to send WhatsApp message: {str(e)}")
        raise