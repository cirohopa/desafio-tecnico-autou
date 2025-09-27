import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("A chave da API da OpenAI não foi encontrada.")
client = OpenAI(api_key=api_key)

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