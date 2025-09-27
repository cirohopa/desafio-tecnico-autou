# backend/test_openai_logic.py

# 1. Importe a função do seu novo arquivo de serviço
from services import analisar_email

# O bloco de execução para teste continua o mesmo!
# Ele agora vai testar a função que está em services.py
if __name__ == "__main__":
    # Exemplo 1: E-mail produtivo
    email_produtivo = """
    Olá equipe,
    Gostaria de verificar o status do ticket #45321 sobre a falha no login.
    Temos alguma previsão de quando será resolvido?
    Obrigado,
    João
    """
    print("\n--- Testando E-mail Produtivo (do arquivo services.py) ---")
    analise1 = analisar_email(email_produtivo)
    if analise1:
        print("Análise Concluída:", analise1)


    # Exemplo 2: E-mail improdutivo
    email_improdutivo = """
    Prezados,
    Gostaria de desejar a todos um Feliz Natal e um próspero Ano Novo!
    Abraços,
    Maria
    """
    print("\n--- Testando E-mail Improdutivo (do arquivo services.py) ---")
    analise2 = analisar_email(email_improdutivo)
    if analise2:
        print("Análise Concluída:", analise2)