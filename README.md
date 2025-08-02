# 🧠 Cursor.AI CLI Replica — Command-Line AI Assistant

[![LangGraph](https://img.shields.io/badge/Built%20with-LangGraph-purple.svg?logo=python&logoColor=white)](https://github.com/langchain-ai/langgraph)
[![LangChain](https://img.shields.io/badge/LangChain-RAG%20Toolkit-blue.svg?logo=python&logoColor=white)](https://github.com/langchain-ai/langchain)
[![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-orange.svg?logo=openai&logoColor=white)](https://www.pinecone.io/learn/retrieval-augmented-generation/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org)
[![AI](https://img.shields.io/badge/AI-Powered%20by%20GPT-green.svg?logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/github/license/AshleyMathias/cursorai-cli)](LICENSE)

A CLI-based AI assistant inspired by **Cursor.AI** — built using LangGraph. It can classify coding vs general queries, execute code-like instructions via shell commands, validate response quality, and even throw back sarcastic roasts for non-code prompts. ⚡

---

## 🚀 Features

- Detects if prompt is a *coding* or *general* query
- Uses **LangGraph** to route and manage logic flows
- Executes shell commands for CLI-based coding tasks
- Validates generated code against original question
- Jokes around for non-coding/general queries 😄
- No UI needed — all CLI, all fast

---

## 🖼️ Screenshot

| Terminal Interaction |
|----------------------|
| ![CLI Screenshot](screenshots/cli_demo.png) |

---

## 🧱 Tech Stack

- `LangGraph` (LangChain's stateful graph engine)
- `OpenAI GPT-4 / GPT-3.5`
- `Python 3.10+`
- `Pydantic`, `TypedDict`
- `os.system` for local command execution

---

## 🛠️ Installation

```bash
git clone https://github.com/AshleyMathias/cursorai-cli.git
cd cursorai-cli
