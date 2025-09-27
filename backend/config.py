from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Define que esperamos uma variável de ambiente chamada OPENAI_API_KEY
    OPENAI_API_KEY: str

    # Diz ao Pydantic para carregar as variáveis de um arquivo .env
    model_config = SettingsConfigDict(env_file=".env")

# Cria uma instância única das configurações que será usada em todo o projeto
settings = Settings()