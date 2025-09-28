from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# 1. Importa nossos modelos do novo arquivo de schemas
from schemas import EmailRequest, EmailResponse
from services import analisar_email, extrair_texto_de_pdf, extrair_texto_de_txt

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

# NOVO ENDPOINT PARA ARQUIVOS
@app.post("/analisar-arquivo", response_model=EmailResponse)
async def analisar_arquivo(file: UploadFile = File(...)):
    """
    Recebe um arquivo (.pdf ou .txt), extrai o texto e o analisa.
    """
    file_bytes = await file.read()
    texto_extraido = None

    if file.content_type == 'application/pdf':
        texto_extraido = extrair_texto_de_pdf(file_bytes)
    elif file.content_type == 'text/plain':
        texto_extraido = extrair_texto_de_txt(file_bytes)
    else:
        raise HTTPException(status_code=400, detail=f"Tipo de arquivo '{file.content_type}' inválido. Por favor, envie um PDF ou TXT.")

    if texto_extraido is None or not texto_extraido.strip():
        raise HTTPException(status_code=400, detail="Não foi possível extrair texto do arquivo enviado. O arquivo pode estar vazio ou ser uma imagem.")

    # REUTILIZANDO nossa lógica principal!
    resultado = analisar_email(texto_extraido)

    if resultado is None:
        raise HTTPException(status_code=503, detail="O serviço de análise de e-mail está indisponível no momento.")

    return resultado