# Minicurso: Ollama Cloud + RAG com ChromaDB

Repositório com o código que estou desenvolvendo como aluno do minicurso de **Ollama Cloud + RAG com ChromaDB**, oferecido na **Semana da Informática 2026** do **Instituto Federal de São Paulo (IFSP), campus Araraquara**. O curso ensina a usar modelos de linguagem hospedados no Ollama Cloud e a construir um sistema de **RAG** (*Retrieval-Augmented Generation*) com o **ChromaDB** como banco de dados vetorial.

> 🚧 **Curso em andamento.** O conteúdo atual corresponde apenas à **Aula 1**. O repositório será atualizado conforme eu avançar nas próximas aulas.

## Progresso

| Aula | Tema | Status |
|---|---|---|
| 1 | Conexão com o Ollama Cloud e chat com streaming | ✅ Concluída |
| 2+ | Embeddings, ChromaDB e RAG | ⏳ A fazer |

## Aula 1: o que foi feito

- Configuração do ambiente (venv, `.env` com a chave de API).
- Conexão com o Ollama Cloud usando a biblioteca Python `ollama`, autenticando com `OLLAMA_API_KEY`.
- Chat com o modelo `gpt-oss:20b-cloud` usando mensagens com papéis (`system` e `user`).
- Exibição da resposta em *streaming*, com efeito de "digitação".

## Estrutura

| Arquivo | Descrição |
|---|---|
| `config.py` | Cria o cliente do Ollama Cloud (host e autenticação) e define o modelo usado. |
| `01_chat.py` | Exemplo da aula 1: chat com *system prompt* e resposta em *streaming*. |
| `.env.example` | Modelo do arquivo de variáveis de ambiente. |

## Pré-requisitos

- Python 3.12 ou superior
- Conta no [Ollama](https://ollama.com) e uma chave de API (*Settings → API keys*)

## Como executar

```bash
# Ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Dependências
pip install ollama python-dotenv

# Chave de API
cp .env.example .env             # depois edite o .env e preencha OLLAMA_API_KEY

# Rodar o exemplo
python 01_chat.py
```

O script pergunta *"quantos dedos tem um elefante?"*, pedindo que o modelo responda como um pirata, e imprime a resposta aos poucos.

> ⚠️ O `.env` está no `.gitignore`. Nunca versione sua chave de API.

## Tecnologias

- [Ollama Cloud](https://ollama.com)
- [ollama-python](https://github.com/ollama/ollama-python)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [ChromaDB](https://www.trychroma.com) (previsto para as próximas aulas)
