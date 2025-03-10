from fastapi import APIRouter, HTTPException, Form
from adapters.whatsapp_adapter import WhatsAppAdapter
from ia_model.load_model import get_model_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/messages")
async def receive_message(Body: str = Form()):
    whatsapp_adapter = WhatsAppAdapter()
   

    model_response = get_model_response(Body)
    print(model_response)
    response = whatsapp_adapter.send_message("+50683962643", model_response)
    
    return {"message": model_response}


@router.get("/{id_chat}")
async def get_chat(id_chat: int):
    return {"message": f"Chat {id_chat}"}
