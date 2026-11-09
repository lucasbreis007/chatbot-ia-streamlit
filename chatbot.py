# Chatbot com IA (Aula 3 da Jornada Python)
#
# Passo 1 - Título
# Passo 2 - Campo de mensagem (input)
# Passo 3 - Quando o usuário mandar mensagem:
#     - mostrar a mensagem na conversa
#     - mandar a mensagem para a IA responder
#     - mostrar a resposta da IA
#
# Instalar as bibliotecas: pip install -r requirements.txt
# Rodar o chatbot:         streamlit run chatbot.py

import streamlit as st
from openai import OpenAI

# Configurações: se o modelo mudar no futuro, é só trocar aqui
URL_API = 'https://generativelanguage.googleapis.com/v1beta/openai'
MODELO = 'gemini-flash-lite-latest'

st.write('### Chat de IA do Lucas')

# Chave da API: cada pessoa cola a sua na barra lateral.
# Ela fica só na memória do navegador durante o uso e nunca é salva em arquivo.
chave_api = st.sidebar.text_input('Chave da API (Google AI Studio)', type='password')
st.sidebar.caption('Crie uma chave grátis em aistudio.google.com e cole aqui.')

# Histórico de mensagens
if not 'lista_mensagem' in st.session_state:
    st.session_state['lista_mensagem'] = []

mensagem_usuario = st.chat_input('Escreva sua mensagem aqui')

for mensagem in st.session_state['lista_mensagem']:
    quem_enviou = mensagem['role']
    texto_mensagem = mensagem['content']
    st.chat_message(quem_enviou).write(texto_mensagem)


if mensagem_usuario:
    if not chave_api:
        st.warning('Cole a sua chave da API na barra lateral para conversar.')
    else:
        # Exibe a mensagem na tela
        # user -> usuário
        # assistant -> chatbot / IA
        st.chat_message('user').write(mensagem_usuario)
        mensagem1 = {'role': 'user', 'content': mensagem_usuario}

        # Pega a resposta da IA. A mensagem do usuário só entra no histórico
        # depois que a IA responde, para um erro não deixar uma pergunta sem resposta.
        try:
            modelo_ia = OpenAI(api_key=chave_api, base_url=URL_API)
            resposta_modelo = modelo_ia.chat.completions.create(
                messages=st.session_state['lista_mensagem'] + [mensagem1],
                model=MODELO
            )
            resposta_ia = resposta_modelo.choices[0].message.content
        except Exception as erro:
            st.error(f'Não foi possível obter a resposta da IA. '
                     f'Confira a chave da API e o modelo ({MODELO}). Detalhe: {erro}')
        else:
            # Envia a resposta para o usuário e guarda as duas mensagens
            st.chat_message('assistant').write(resposta_ia)
            mensagem2 = {'role': 'assistant', 'content': resposta_ia}
            st.session_state['lista_mensagem'].append(mensagem1)
            st.session_state['lista_mensagem'].append(mensagem2)
