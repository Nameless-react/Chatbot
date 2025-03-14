from fastapi import APIRouter, HTTPException, Form
from senders.message_sender import message_sender
from senders.whatsapp_sender import send_whatsapp
from ia_model.load_model import get_model_response
from typing import Dict

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/messages")
async def receive_message(Body: str = Form(), From: str = Form()):
    
   

    model_response: str = get_model_response(Body)
    print(model_response)
    response: Dict[str, str] = message_sender(send_whatsapp, From, model_response)
    
    return {"message": model_response}


@router.get("/{id_chat}")
async def get_chat(id_chat: int):
    return {"message": f"Chat {id_chat}"}
