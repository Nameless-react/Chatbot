from ollama import Client
import logging
from pydantic import BaseModel
from typing import Optional

logger = logging.getLogger(__name__)

class ModelConfig(BaseModel):
    model_name: str = "llama3.1"
    max_tokens: int = 100
    temperature: float = 0.7

def get_model_response(prompt: str, config: Optional[ModelConfig] = ModelConfig()) -> str:
    """
    Generates the AI model's response.

    Args:
        prompt (str): The user's message.
        config (optional): Model configuration settings.

    Returns:
        str: The model's response.
    """

    if not prompt or prompt.strip() == "":
        raise ValueError("Prompt cannot be empty")

    system_prompt = (
        "Eres un asistente experto en soporte técnico de inteligencia artificial, "
        "especializado en programación, modelos de lenguaje y soluciones de desarrollo. "
        "Responde de manera concisa y técnica, proporcionando ejemplos de código y explicaciones detalladas "
        "cuando sea necesario. Solo responderás preguntas relacionadas con IA, aprendizaje automático, "
        "procesamiento de lenguaje natural y programación en general. Si una consulta no está relacionada con estos temas, "
        "indica educadamente que solo puedes ayudar en temas de inteligencia artificial y desarrollo de software."
    )
    
    try:
        client = Client(host="http://ollama:11434")
        logger.info(f"Requesting response from {config.model_name} model")
        response = client.chat(
            model=config.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            options={
                "max_tokens": config.max_tokens,
                "temperature": config.temperature
            }
        )
        
        content = response["message"]["content"]
        return content
    except Exception as e:
        logger.error(f"Model inference error: {str(e)}")
        raise