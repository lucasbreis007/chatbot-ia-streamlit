# 🤖 Chatbot com IA (Python + Streamlit)

Chatbot que roda no navegador, conversa com o modelo **Gemini** do Google e **lembra do histórico da conversa**. Feito só com Python: o Streamlit cria a interface (front-end) e a lógica (back-end) no mesmo arquivo.

Projeto baseado na **Aula 3 da Jornada Python (Hashtag Treinamentos)**.

## O que ele faz

1. Mostra um chat no navegador com título e campo de mensagem
2. Exibe a pergunta do usuário na conversa
3. Envia a pergunta, junto com todo o histórico, para a IA
4. Exibe a resposta da IA e guarda tudo na memória da sessão, então a conversa mantém o contexto

## Melhorias em relação ao código da aula

| Antes (código da aula) | Agora |
|---|---|
| Chave da API escrita dentro do código | Cada pessoa cola a própria chave na barra lateral do app. Ela não é salva em arquivo nenhum |
| Erro da API derrubava o chat com uma tela vermelha | Aparece um aviso claro e a conversa continua funcionando |
| Pergunta ficava no histórico mesmo sem resposta (e a próxima enviava duas perguntas seguidas) | A pergunta só entra no histórico depois que a IA responde |
| Modelo escrito no meio do código | `URL_API` e `MODELO` ficam no topo do arquivo, fáceis de trocar |
| Arquivo `vtnc3.py` | `chatbot.py`, mais claro |
| Sem requirements, README nem .gitignore | Incluídos, com `.env` e `secrets.toml` ignorados pelo Git |

## Estrutura do projeto

```
chatbot-ia-streamlit/
├── chatbot.py          # O chatbot (todo o código)
├── requirements.txt    # Bibliotecas necessárias
├── imagens/            # Prints usados neste README
├── .gitignore
└── README.md
```

## Como rodar (Windows + VS Code)

Precisa do [Python 3](https://www.python.org/downloads/) (marque *Add Python to PATH* na instalação) e do [VS Code](https://code.visualstudio.com/).

**1. Baixe o projeto** e abra a pasta no VS Code (**Arquivo > Abrir Pasta**).

**2. Instale as bibliotecas.** No terminal do VS Code (**Terminal > Novo Terminal**), em **uma linha só**:

```bash
pip install -r requirements.txt
```

Se o Windows disser que `pip` não é reconhecido, use `py -m pip install -r requirements.txt`.

**3. Crie sua chave da API (grátis).**
1. Entre em [aistudio.google.com](https://aistudio.google.com) e faça login com sua conta Google
2. Abra **Chaves de API** (*Get API key*) e crie uma chave
3. Copie a chave. **Não compartilhe nem publique essa chave**

**4. Rode o chatbot:**

```bash
streamlit run chatbot.py
```

Não use o botão de "executar" do VS Code: o Streamlit precisa desse comando. O navegador abre em `http://localhost:8501`.

**5. Cole sua chave** no campo da barra lateral (à esquerda) e converse. Para parar o programa, aperte `Ctrl+C` no terminal.

## Prints

*(Os prints do chatbot funcionando serão adicionados aqui.)*

## Como o código funciona

| Trecho | O que faz |
|---|---|
| `st.write('### ...')` | Mostra o título (o `###` é Markdown) |
| `st.sidebar.text_input(..., type='password')` | Campo da chave na barra lateral, com o texto escondido |
| `st.session_state['lista_mensagem']` | Memória da conversa. O Streamlit roda o código todo a cada interação, então sem isso a lista seria apagada |
| `st.chat_input` | Campo onde o usuário digita |
| `for mensagem in ...` | Redesenha o histórico inteiro a cada execução |
| `modelo_ia.chat.completions.create(...)` | Envia a lista de mensagens para a IA e recebe a resposta |
| `try / except / else` | Se der erro, mostra o aviso. Se der certo, mostra a resposta e guarda as duas mensagens |

Cada mensagem é um dicionário `{'role': ..., 'content': ...}`: `role` diz quem falou (`user` ou `assistant`) e `content` é o texto. O chat inteiro é uma lista desses dicionários, o formato que as IAs de conversa esperam.

## Segurança

- A chave **nunca** fica no código nem em arquivos do projeto. Cada pessoa usa a sua
- O `.gitignore` bloqueia `.env` e `.streamlit/secrets.toml`, caso você queira guardar a chave num desses arquivos por conta própria
- Se uma chave vazar, apague-a no Google AI Studio e crie outra

## Limitações

- A conversa **some ao atualizar a página** (a memória é da sessão do navegador, não é salva em arquivo ou banco de dados)
- Cada pergunta reenvia o histórico inteiro, então conversas muito longas consomem mais da cota gratuita
- O modelo `gemini-flash-lite-latest` pode mudar ou sair do ar no futuro. Se aparecer erro de modelo, troque o valor de `MODELO` no topo do `chatbot.py`
- Não há instruções de comportamento (system prompt): a IA responde de forma geral

## Tecnologias

- Python 3
- [Streamlit](https://streamlit.io/): interface web
- [OpenAI (biblioteca Python)](https://github.com/openai/openai-python): usada para falar com a API do Gemini, que é compatível com esse formato
- Google Gemini (via Google AI Studio)
