from fastapi import APIRouter
from adapters.whatsapp_adapter import WhatsAppAdapter



router = APIRouter(prefix="/chat", tags=["Chat"])

@router.get("/")
async def receive_message():
    whatsapp_adapter = WhatsAppAdapter()
    response = whatsapp_adapter.send_message("+50683962643", "Hola")
    # print(response.status_code)
    # print(response.json())
    return {"message": "Lista de usuarios"}


@router.get("/{id_chat}")
async def get_chat(id_chat: int):
    return {"message": f"Chat {id_chat}"}
