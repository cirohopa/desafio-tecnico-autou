# backend/schemas.py
from pydantic import BaseModel

class EmailRequest(BaseModel):
    texto: str

class EmailResponse(BaseModel):
    categoria: str
    sugestao_resposta: str