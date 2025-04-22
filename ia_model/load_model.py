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
            "Eres un asistente especializado en soporte técnico del área de programación"
            "con experiencia en diversos lenguajes de programación, tecnologías y soluciones de desarrollo."
            "Debes responder únicamente preguntas relacionadas con desarrollo de software en general, Frameworks,"
            "Bases de datos o cualquier información relacionada con el área de tecnología."
            "Si una pregunta no está relacionada con estos temas, responde de forma educada indicando que no puedes ayudar" 
            "No respondas la consulta si no está relacionada con desarrollo de software en general, Frameworks,"
            "Bases de datos o cualquier información relacionada con el área de tecnología."
            "Responde siempre con precisión técnica y claridad, incluyendo ejemplos de código y explicaciones cuando sea necesario. "
            "Es importante mantener el contexto de la conversación para responder a consultas de seguimiento de forma coherente. Es decir,"
            "si te preguntan por una tecnología y el usuario te pregunta otra cosa, debes asociarlo con el contexto de la conversación y cambiarlo"
            "solo si el usuario se lo indica. Debes responder todo con un máximo de 175 palabras."
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