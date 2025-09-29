import json
from openai import OpenAI

from pypdf import PdfReader
import io

from config import settings

# A validação da chave foi feita pelo 'config.py'.
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def analisar_email(texto_email: str) -> dict | None:
    prompt_sistema = """
    Você é um assistente de produtividade altamente eficiente, especializado em analisar e-mails.
    Sua tarefa é classificar um e-mail em uma de duas categorias: 'Produtivo' ou 'Improdutivo'.
    - 'Produtivo': E-mails que requerem uma ação, resposta ou contêm informação importante.
    - 'Improdutivo': E-mails de marketing, felicitações, agradecimentos genéricos ou spam.

    Além de classificar, você deve gerar uma sugestão de resposta curta e profissional, apropriada para a categoria.

    Sua resposta final deve ser estritamente um objeto JSON, sem nenhum texto ou explicação adicional antes ou depois.
    O objeto JSON deve ter a seguinte estrutura:
    {
      "categoria": "...",
      "sugestao_resposta": "..."
    }
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": texto_email}
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )
        resultado_json_str = response.choices[0].message.content
        return json.loads(resultado_json_str)
    except Exception as e:
        print(f"!!! Ocorreu um erro ao chamar a API da OpenAI: {e}")
        return None
    
def extrair_texto_de_pdf(file_bytes: bytes) -> str | None:
    """
    Recebe os bytes de um arquivo PDF e extrai o texto de todas as páginas.
    """
    try:
        pdf_file = io.BytesIO(file_bytes)
        reader = PdfReader(pdf_file)
        texto_completo = ""
        for page in reader.pages:
            texto_extraido = page.extract_text()
            if texto_extraido:
                texto_completo += texto_extraido + "\n"
        return texto_completo
    except Exception as e:
        print(f"!!! Erro ao processar o PDF: {e}")
        return None

def extrair_texto_de_txt(file_bytes: bytes) -> str | None:
    """
    Recebe os bytes de um arquivo TXT e decodifica para texto.
    """
    try:
        # Tenta decodificar como UTF-8, o padrão mais comum
        return file_bytes.decode('utf-8')
    except UnicodeDecodeError:
        try:
            # Tenta outros formatos comuns se o UTF-8 falhar
            return file_bytes.decode('latin-1')
        except Exception as e:
            print(f"!!! Erro ao decodificar o TXT: {e}")
            return None
    except Exception as e:
        print(f"!!! Erro geral ao processar o TXT: {e}")
        return None