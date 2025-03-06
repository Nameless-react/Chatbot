from fastapi import FastAPI, Request
import requests
from routes.ia_routes import router as chat_router


app = FastAPI()
app.include_router(chat_router)

@app.get("/")
async def root():
    return { "message": "Hello world" }