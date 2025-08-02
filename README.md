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
```
## Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
## Install dependencies
```bash
pip install -r requirements.txt
```
## Set your OpenAI API key

```bash
export OPENAI_API_KEY=your-key-here  # Or store in .env
```
## Run the assistant

```bash
python cursorai.py
```

---

## 📂 Project Structure

cursorai-cli/
├── cursorai.py               # Main CLI LangGraph agent
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
└── screenshots/
    └── cli_demo.png          # Optional screenshot for README

---

## ✨ Sample Use Case
Build your own AI terminal assistant like Cursor.ai! This project handles user queries, decides if it's code-related, executes instructions, and verifies correctness — all from your terminal.

#💡 Try prompts like:

create a folder named test_files
how to write a bash loop
how to enter Google without DSA? (😂 roasted!)

Use it for:
- Fast prototyping with shell-based AI
- Agent routing + validation logic
- CLI-based dev tools and AI hacks

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

If you’d like to:
- Suggest improvements
- Report bugs
- Add new features or integrations

Feel free to fork the repository and submit a pull request.
Please follow clean commit practices and open issues with context.

Let’s build cool dev tools together 🚀

---

## 📄 License
This project is licensed under the MIT License.

You're free to use, modify, and share the codebase — just retain attribution.
See the LICENSE file for full details.

<div align="center">
📘 Built for developers who love the terminal and want AI to code, joke, and validate like a true teammate.

<br/>
🔗 Connect with me
<a href="https://www.linkedin.com/in/ashleymathias10" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Ashley%20Mathias-blue?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
   
<a href="mailto:ashleymathias100@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-ff69b4?style=flat&logo=gmail&logoColor=white" alt="Email"></a>
   
<a href="https://github.com/AshleyMathias"><img src="https://img.shields.io/badge/GitHub-@AshleyMathias-181717?style=flat&logo=github&logoColor=white" alt="GitHub"></a>

<br/><br/>

💻 Terminal-first. Fun. Fast. Functional.
Let’s build something legendary.

</div> ```
