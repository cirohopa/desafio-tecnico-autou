from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Importa nossa função de lógica do outro arquivo
from services import analisar_email

# Cria a aplicação FastAPI
app = FastAPI()

# --- Configuração do CORS ---
# Isso é super importante para permitir que seu frontend (que rodará em um endereço diferente)
# possa fazer requisições para este backend.
origins = ["*"] # Para desenvolvimento. Em produção, seria o link do seu site.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Modelos de Dados (Pydantic) ---
# Define como serão os dados que a API recebe e envia

class EmailRequest(BaseModel):
    texto: str

class EmailResponse(BaseModel):
    categoria: str
    sugestao_resposta: str

# --- Endpoint da API ---
# Este é o "endereço" que nosso frontend vai chamar

@app.post("/analisar-email", response_model=EmailResponse)
def analisar(request: EmailRequest):
    """
    Recebe um texto de e-mail, analisa usando a OpenAI e retorna a categoria e uma sugestão de resposta.
    """
    if not request.texto or not request.texto.strip():
        raise HTTPException(status_code=400, detail="O texto do e-mail não pode estar vazio.")

    # Chama a nossa função que faz o trabalho pesado
    resultado = analisar_email(request.texto)

    if resultado is None:
        raise HTTPException(status_code=503, detail="O serviço de análise de e-mail está indisponível no momento.")

    return resultado