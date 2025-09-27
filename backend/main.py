from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# 1. Importa nossos modelos do novo arquivo de schemas
from schemas import EmailRequest, EmailResponse
from services import analisar_email

app = FastAPI()

# --- Configuração do CORS ---
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Endpoint da API ---
@app.post("/analisar-email", response_model=EmailResponse)
def analisar(request: EmailRequest):
    """
    Recebe um texto de e-mail, analisa usando a OpenAI e retorna a categoria e uma sugestão de resposta.
    """
    if not request.texto or not request.texto.strip():
        raise HTTPException(status_code=400, detail="O texto do e-mail não pode estar vazio.")

    resultado = analisar_email(request.texto)

    if resultado is None:
        raise HTTPException(status_code=503, detail="O serviço de análise de e-mail está indisponível no momento.")

    return resultado