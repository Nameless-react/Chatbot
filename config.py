from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "ACCESS_TOKEN": os.getenv("ACCESS_TOKEN"),
    "VERSION": os.getenv("VERSION"),
    "PHONE_NUMBER_ID": os.getenv("PHONE_NUMBER_ID"),
    "ACCOUNT_SID": os.getenv("ACCOUNT_SID"),
    "AUTH_TOKEN": os.getenv("AUTH_TOKEN")
}
