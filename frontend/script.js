// frontend/script.js (versão refatorada)

document.addEventListener('DOMContentLoaded', () => {
    // --- 1. Seleção dos Elementos do DOM ---
    const emailInput = document.getElementById('email-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resultContainer = document.getElementById('result-container');
    const resultContent = document.getElementById('result-content');

    // --- 2. Configurações ---
    const API_URL = 'http://127.0.0.1:8000/analisar-email';

    // --- 3. Funções Principais ---

    /**
     * Função principal que é chamada quando o botão é clicado.
     */
    const handleAnalyzeClick = async () => {
        const emailText = emailInput.value;
        if (!emailText.trim()) {
            alert('Por favor, insira o texto de um e-mail.');
            return;
        }

        setLoadingState(true);
        try {
            const data = await callApi(emailText);
            displayResult(data);
        } catch (error) {
            displayError(error.message);
        } finally {
            setLoadingState(false);
        }
    };

    /**
     * Envia a requisição para a API backend.
     * @param {string} text - O texto do e-mail para analisar.
     * @returns {Promise<object>} - Os dados da resposta da API.
     */
    const callApi = async (text) => {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ texto: text }),
        });
        if (!response.ok) {
            // Lança um erro mais amigável se a comunicação falhar
            throw new Error('Não foi possível conectar ao servidor de análise. Verifique se ele está ativo.');
        }
        return response.json();
    };

    /**
     * Atualiza a interface para mostrar o estado de carregamento.
     * @param {boolean} isLoading - True se estiver carregando, false caso contrário.
     */
    const setLoadingState = (isLoading) => {
        analyzeBtn.disabled = isLoading;
        analyzeBtn.textContent = isLoading ? 'Analisando...' : 'Analisar E-mail';
        if (isLoading) {
            resultContainer.classList.add('hidden');
        }
    };

    /**
     * Exibe o resultado da análise na tela.
     * @param {object} data - O objeto com 'categoria' e 'sugestao_resposta'.
     */
    const displayResult = (data) => {
        resultContent.innerHTML = `
            <p><strong>Categoria:</strong> ${data.categoria}</p>
            <p><strong>Sugestão de Resposta:</strong> ${data.sugestao_resposta}</p>
        `;
        resultContainer.classList.remove('hidden');
    };

    /**
     * Exibe uma mensagem de erro na tela.
     * @param {string} message - A mensagem de erro a ser exibida.
     */
    const displayError = (message) => {
        resultContent.innerHTML = `<p class="error-message"><strong>Erro:</strong> ${message}</p>`;
        resultContainer.classList.remove('hidden');
    };

    // --- 4. Event Listener ---
    analyzeBtn.addEventListener('click', handleAnalyzeClick);
});