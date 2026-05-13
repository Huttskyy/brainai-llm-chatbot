import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Configuração da API Key
api_key = [Sua key]

# Códigos de cores (ANSI)
AMARELO = '\033[1;33m'
AZUL_CLARO = '\033[1;36m'
ROXO = '\033[1;35m'
RESET = '\033[0m'

# Seleciona o modelo
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Informações extraídas da fonte (Wikipedia - Filme)
CONTEUDO_WIKI = """
Filme é um produto audiovisual formado por imagens fixas que projetadas geram sensação de movimento.
Gêneros principais: Ação, Animação, Aventura, Comédia, Documentário, Drama, Fantasia, Faroeste, Ficção Científica, Musical, Romance, Terror, Super-herói, etc.
Produção: Pré-produção (planejamento), Produção (gravação) e Pós-produção (edição/efeitos).
História: Precursores incluem lanterna mágica e teatro de sombras. O cinema se desenvolveu no fim do século XIX com celuloide.
Duração: Longa-metragem (mais de 1h) e Curta-metragem (menos de 1h).
"""

def resposta_bot(mensagens, nome_usuario):
    # Prompt restritivo: a IA só pode usar o CONTEUDO_WIKI
    system_prompt = (
        f"Você é o assistente BrainAI conversando com {nome_usuario}. "
        "REGRAS CRÍTICAS: Use APENAS as informações abaixo para responder. "
        "Não use nenhum conhecimento externo. Se a resposta não estiver no texto, "
        "responda exatamente: 'resposta não encontrada'.\n\n"
        f"CONTEÚDO DE REFERÊNCIA:\n{CONTEUDO_WIKI}"
    )
    
    mensagens_modelo = [('system', system_prompt)]
    mensagens_modelo += mensagens 
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

# --- Início da Interação ---
print('--- Bem-vindo à BrainAI ---')

# Nome do usuário em AMARELO
nome = input('Antes de começar, qual é o seu nome? ' + AMARELO)
print(RESET, end="") 

print(f'Olá, {nome}!')

mensagens = []
primeira_pergunta = True 

while True:
    print("") 
    
    if primeira_pergunta:
        print("O que você deseja saber sobre filmes?")
        primeira_pergunta = False
    
    # Pergunta do usuário em AZUL CLARO
    pergunta = input('Pergunta- ' + AZUL_CLARO)
    print(RESET, end="") 
    
    if pergunta.lower() == 'x':
        break
        
    mensagens.append(('user', pergunta))
    
    # Resposta
    resposta = resposta_bot(mensagens, nome)
    mensagens.append(('assistant', resposta))
    
    # Exibição em ROXO
    print(f'\nResposta- {ROXO}{resposta}{RESET}')
    print("-" * 50)

# Finalização
print(f'\nAté logo, {nome}!')
