document.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.getElementById('email-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resultContainer = document.getElementById('result-container');
    const resultContent = document.getElementById('result-content');

    // O endereço da nossa API rodando localmente
    const API_URL = 'http://127.0.0.1:8000/analisar-email';

    analyzeBtn.addEventListener('click', async () => {
        const emailText = emailInput.value;

        if (!emailText.trim()) {
            alert('Por favor, insira o texto de um e-mail.');
            return;
        }

        // Desabilita o botão e mostra um estado de "carregando"
        analyzeBtn.disabled = true;
        analyzeBtn.textContent = 'Analisando...';
        resultContainer.classList.add('hidden');

        try {
            // 1. Faz a requisição para a API (o nosso "garçom" FastAPI)
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ texto: emailText }), // Envia o texto no formato JSON esperado
            });

            if (!response.ok) {
                // Se a resposta não for OK (ex: erro 503), lança um erro
                throw new Error(`Erro na API: ${response.statusText}`);
            }

            // 2. Pega a resposta da API e converte para JSON
            const data = await response.json();

            // 3. Mostra os resultados na tela
            resultContent.innerHTML = `
                <p><strong>Categoria:</strong> ${data.categoria}</p>
                <p><strong>Sugestão de Resposta:</strong> ${data.sugestao_resposta}</p>
            `;
            resultContainer.classList.remove('hidden');

        } catch (error) {
            // Em caso de erro, mostra um alerta
            console.error('Falha ao analisar e-mail:', error);
            alert('Não foi possível analisar o e-mail. Verifique se o servidor backend está rodando e tente novamente.');
        } finally {
            // Reabilita o botão, independentemente do resultado
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = 'Analisar E-mail';
        }
    });
});