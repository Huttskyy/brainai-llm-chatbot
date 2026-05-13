# brainai-llm-chatbot
# Trabalho acadêmico 
# Chatbot terminal baseado em LLM utilizando LangChain e Groq API.

# BrainAI - LLM Chatbot

Assistente conversacional em terminal desenvolvido com Python, LangChain e Groq API.

O projeto utiliza engenharia de prompts para restringir respostas apenas ao conteúdo fornecido, simulando um sistema de consulta contextual controlado.

---

## Tecnologias

- Python
- LangChain
- Groq API
- Llama 3.3 70B
- Prompt Engineering

---

## Funcionalidades

- Chat em terminal
- Memória de conversa
- Restrição contextual
- Respostas controladas por prompt
- Personalização com nome do usuário

---

## Objetivo do projeto

Praticar integração com LLMs, engenharia de prompts e desenvolvimento de aplicações conversacionais.

---

## Como executar
1. Instalar as bibliotecas

Abra o terminal no VS Code, CMD ou colab e rode:
pip install langchain langchain-groq pypdf

2. Pegar a API Key da Groq
-Entre em:
-Groq Console
-Faça login
-Pode usar:
-Google;
-GitHub;
-email.
-Vá em:
-API Keys
-Clique:
-Create API Key
3. Colocar a API Key no código
      
4. Como usar PDF no projeto
Coloque o PDF na mesma pasta do projeto
```bash
pip install langchain langchain-groq
python main.py
