document.addEventListener('DOMContentLoaded', () => {
    // --- 1. Seleção dos Elementos do DOM ---
    const emailInput = document.getElementById('email-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resultContainer = document.getElementById('result-container');
    const resultContent = document.getElementById('result-content');
    const fileInput = document.getElementById('file-input');
    const fileInfoDiv = document.getElementById('file-info'); // -- NOVO --

    // --- 2. Configurações ---
    const API_BASE_URL = 'http://127.0.0.1:8000';

    // --- 3. Funções Principais ---

    const handleAnalyzeClick = async () => {
        const emailText = emailInput.value;
        const file = fileInput.files[0];

        if (!emailText.trim() && !file) {
            alert('Por favor, insira um texto ou selecione um arquivo.');
            return;
        }

        setLoadingState(true);
        try {
            let data;
            if (file) {
                const formData = new FormData();
                formData.append('file', file);
                data = await callApi('/analisar-arquivo', formData);
            } else {
                data = await callApi('/analisar-email', { texto: emailText });
            }
            displayResult(data);
        } catch (error) {
            displayError(error.message);
        } finally {
            setLoadingState(false);
            clearFileInput(); // -- ALTERAÇÃO --
        }
    };

    const callApi = async (endpoint, body) => {
        const url = API_BASE_URL + endpoint;
        let options = { method: 'POST' };

        if (body instanceof FormData) {
            options.body = body;
        } else {
            // Para texto, enviamos JSON.
            options.headers = { 'Content-Type': 'application/json' };
            options.body = JSON.stringify(body);
        }

        const response = await fetch(url, options);
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({ detail: 'Erro desconhecido no servidor.' }));
            throw new Error(errorData.detail);
        }
        return response.json();
    };

    // -- INÍCIO DO NOVO BLOCO DE CÓDIGO --
    /**
     * Limpa a seleção de arquivo e esconde o display de informação.
     */
    const clearFileInput = () => {
        fileInput.value = ''; // Limpa o input de arquivo
        fileInfoDiv.classList.add('hidden'); // Esconde o display
    };

    /**
     * Ouve por mudanças no input de arquivo.
     */
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            // Mostra o nome do arquivo e um botão para limpar
            fileInfoDiv.innerHTML = `
                <span>📄 ${file.name}</span>
                <button class="clear-file-btn" title="Remover arquivo">X</button>
            `;
            fileInfoDiv.classList.remove('hidden');

            // Adiciona o evento de clique ao novo botão 'X'
            fileInfoDiv.querySelector('.clear-file-btn').addEventListener('click', () => {
                clearFileInput();
            });

            // Opcional: Limpa o textarea se um arquivo for selecionado
            emailInput.value = '';

        } else {
            fileInfoDiv.classList.add('hidden');
        }
    });
    // -- FIM DO NOVO BLOCO DE CÓDIGO --

    const setLoadingState = (isLoading) => {
        analyzeBtn.disabled = isLoading;
        analyzeBtn.textContent = isLoading ? 'Analisando...' : 'Analisar';
        if (isLoading) {
            resultContainer.classList.add('hidden');
        }
    };

    const displayResult = (data) => {
        resultContent.innerHTML = `
            <p><strong>Categoria:</strong> ${data.categoria}</p>
            <p><strong>Sugestão de Resposta:</strong> ${data.sugestao_resposta}</p>
        `;
        resultContainer.classList.remove('hidden');
    };

    const displayError = (message) => {
        resultContent.innerHTML = `<p class="error-message"><strong>Erro:</strong> ${message}</p>`;
        resultContainer.classList.remove('hidden');
    };

    // --- 4. Event Listener ---
    analyzeBtn.addEventListener('click', handleAnalyzeClick);
});