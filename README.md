# 📧 Analisador de E-mails com IA - Desafio Técnico AutoU
Este projeto é uma solução completa para o desafio técnico do processo seletivo da AutoU. Trata-se de uma aplicação web full-stack que utiliza Inteligência Artificial para classificar e-mails como "Produtivos" ou "Improdutivos" e sugerir respostas automáticas, otimizando o fluxo de trabalho de equipes que lidam com um alto volume de mensagens.

## 🚀 Aplicação Online
A aplicação está hospedada na nuvem e pode ser acessada através do link a seguir:

Acesse o Analisador de E-mails [aqui](https://autou-frontend-fnqw.onrender.com)!

- Nota: A aplicação está hospedada no plano gratuito do Render. O primeiro acesso pode levar de 30 a 60 segundos para ativar o servidor. Se encontrar um erro na primeira tentativa, por favor, aguarde um momento e tente novamente.

Demonstração Rápida 
![GIF da aplicação analisando arquivo .txt](./assets/analise-de-txt-autou.gif)

## 🎯 Sobre o Projeto
O objetivo foi desenvolver uma ferramenta intuitiva que automatiza a triagem de e-mails. A aplicação permite que o usuário cole o texto de um e-mail ou faça o upload de um arquivo (.pdf ou .txt) para receber uma classificação instantânea e uma sugestão de resposta gerada por IA, liberando tempo da equipe para focar em tarefas mais importantes.

## ✨ Funcionalidades
A aplicação vai além dos requisitos básicos, implementando funcionalidades que melhoram a robustez e a experiência do usuário:
- Análise por Múltiplos Formatos: Análise de texto colado diretamente na interface. Upload e processamento de arquivos .pdf.
- Upload e processamento de arquivos .txt.
- Inteligência Artificial (OpenAI): Classificação do e-mail em Produtivo ou Improdutivo.
- Geração de respostas automáticas contextuais e profissionais. 
- Interface Intuitiva e Reativa: Design Responsivo que se adapta perfeitamente a desktops, tablets e celulares.
- Feedback visual claro do arquivo selecionado, com opção de remoção.
- Estados de "carregamento" para informar o usuário que o processamento está em andamento.
- Tratamento de erros elegante, exibindo mensagens claras na interface em caso de falhas.
- Backend Robusto e Escalável: API construída com FastAPI, seguindo as melhores práticas de desenvolvimento.
- Código estruturado e modularizado (rotas, serviços, schemas, configurações).Validação de dados na entrada e saída da API. 

## 🛠️ Tecnologias Utilizadas
Este projeto foi construído utilizando uma stack moderna e alinhada com as melhores práticas do mercado.
### Backend:
- Linguagem: Python 3.12
- Framework da API: FastAPI
- Inteligência Artificial: OpenAI API (GPT-3.5-Turbo)
- Processamento de PDF: pypdf
- Validação de Dados: Pydantic
- Servidor de Produção: Gunicorn & Uvicorn
- Frontend:Estrutura: HTML5 Semântico
- Estilização: CSS3 (com Media Queries para responsividade)
- Interatividade: JavaScript (Vanilla JS) com Fetch API para comunicação assíncrona.
- Cloud & DevOps:Hospedagem: Render (Web Service para o backend e Static Site para o frontend).
- Controle de Versão: Git & GitHub.Ambiente Virtual: venv.

## ⚙️ Como Executar o Projeto Localmente
Para rodar esta aplicação em sua máquina local, siga os passos abaixo.

### Pré-requisitos:
- Python 3.10 + Um editor de código (ex: VS Code)

- -Uma chave de API da OpenAI

### Passos:
- Clone o repositório: 
```bash
git clone https://github.com/cirohopa/desafio-tecnico-autou.git
cd desafio-tecnico-autou
```
Configure o Backend:
```bash
# Navegue até a pasta do backend
cd backend

# Crie e ative um ambiente virtual
python -m venv venv
.\venv\Scripts\activate  # No Windows

# Instale as dependências
pip install -r requirements.txt

# Crie um arquivo .env na pasta 'backend' e adicione sua chave
# OPENAI_API_KEY="sk-..."

# Inicie o servidor
uvicorn main:app --reload
```
O backend estará rodando em http://127.0.0.1:8000.

- Configure o Frontend: Com o backend rodando, abra o arquivo frontend/index.html em seu navegador.

- Dica: A extensão "Live Server" para o VS Code é recomendada para uma melhor experiência de desenvolvimento.
# 🏛️ Estrutura do Projeto
O projeto segue uma estrutura de monorepo, separando claramente as responsabilidades do backend e do frontend:/autou-desafio
```bash
|-- /backend
|   |-- /venv
|   |-- config.py
|   |-- main.py
|   |-- requirements.txt
|   |-- schemas.py
|   |-- services.py
|   |-- .env
|
|-- /frontend
|   |-- index.html
|   |-- script.js
|   |-- style.css
|
|-- .gitignore
|-- README.md
```
Obrigado pela oportunidade!
 
Ciro Henrique O. P. Almeida

LinkedIn: [Ciro Henrique](www.linkedin.com/in/ciro-henrique)

GitHub: [cirohopa](https://github.com/cirohopa)
