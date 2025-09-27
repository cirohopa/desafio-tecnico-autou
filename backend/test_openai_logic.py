import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configuração Inicial do Cliente OpenAI ---
# Pega a chave da API das variáveis de ambiente
api_key = os.getenv("OPENAI_API_KEY")

# Validação: verifica se a chave da API foi carregada
if not api_key:
    raise ValueError("A chave da API da OpenAI não foi encontrada. Verifique seu arquivo .env.")

# Instancia o cliente da OpenAI
client = OpenAI(api_key=api_key)


def analisar_email(texto_email: str) -> dict:
    """
    Analisa o texto de um e-mail usando a API da OpenAI para classificar
    e sugerir uma resposta, retornando um dicionário Python.
    """
    print(">>> Iniciando análise do e-mail...")

    # Esta é a "engenharia de prompt" que discutimos.
    # É aqui que damos as instruções para a IA.
    prompt_sistema = """
    Você é um assistente de produtividade altamente eficiente, especializado em analisar e-mails.
    Sua tarefa é classificar um e-mail em uma de duas categorias: 'Produtivo' ou 'Improdutivo'.
    - 'Produtivo': E-mails que requerem uma ação, resposta ou contêm informação importante.
    - 'Improdutivo': E-mails de marketing, felicitações, agradecimentos genéricos ou spam.

    Além de classificar, você deve gerar uma sugestão de resposta curta e profissional, apropriada para a categoria.

    Sua resposta DEVE ser um objeto JSON válido, sem nenhum texto ou explicação adicional.
    O JSON deve ter a seguinte estrutura:
    {
      "categoria": "...",
      "sugestao_resposta": "..."
    }
    """

    try:
        # Faz a chamada para a API de Chat Completions
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",  # Um modelo rápido e otimizado para seguir instruções
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": texto_email}
            ],
            temperature=0.2,  # Baixa temperatura para respostas mais consistentes e menos criativas
            response_format={"type": "json_object"} # Força a saída a ser um JSON válido
        )

        # Extrai o conteúdo da resposta, que deve ser uma string JSON
        resultado_json_str = response.choices[0].message.content
        print(">>> Resposta da API recebida.")

        # Converte a string JSON em um dicionário Python
        resultado_final = json.loads(resultado_json_str)
        return resultado_final

    except Exception as e:
        print(f"!!! Ocorreu um erro ao chamar a API da OpenAI: {e}")
        return None


# --- Bloco de Execução Principal para Teste ---
if __name__ == "__main__":
    # Exemplo 1: E-mail produtivo
    email_produtivo = """
    Olá equipe,
    Gostaria de verificar o status do ticket #45321 sobre a falha no login.
    Temos alguma previsão de quando será resolvido?
    Obrigado,
    João
    """
    print("\n--- Testando E-mail Produtivo ---")
    analise1 = analisar_email(email_produtivo)
    if analise1:
        print("Análise Concluída:", analise1)
        # Exemplo de acesso aos dados:
        print("Categoria:", analise1.get("categoria"))
        print("Sugestão:", analise1.get("sugestao_resposta"))


    # Exemplo 2: E-mail improdutivo
    email_improdutivo = """
    Prezados,
    Gostaria de desejar a todos um Feliz Natal e um próspero Ano Novo!
    Abraços,
    Maria
    """
    print("\n--- Testando E-mail Improdutivo ---")
    analise2 = analisar_email(email_improdutivo)
    if analise2:
        print("Análise Concluída:", analise2)
        print("Categoria:", analise2.get("categoria"))
        print("Sugestão:", analise2.get("sugestao_resposta"))