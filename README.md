# 🤖 AI Chatbot GUI (Phi-3 + CustomTkinter)

A modern desktop AI chatbot built using **Python**, powered by **Phi-3 (via Ollama)**, with a clean and responsive GUI using **CustomTkinter**.

---

## 🚀 Features

- 💬 ChatGPT-style interface  
- 👉 User messages aligned to the right  
- 🤖 AI responses aligned to the left  
- 🧠 Context-aware conversation (remembers previous messages)  
- 💾 Chat history stored locally (`chat_history.json`)  
- ⚡ Smooth UI with threaded responses (no freezing)  
- ⏳ "Bot is typing..." indicator  
- 🔒 Send button disabled while processing  
- 🧼 Clean chat screen on startup (history hidden but used internally)

---

## 🛠️ Tech Stack

- **Python**
- **CustomTkinter** (GUI)
- **LangChain**
- **Ollama**
- **Phi-3 Model**

---

## 📦 Installation Guide

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2️⃣ Create a virtual environment
python -m venv .venv

Activate it:

Windows:

.\.venv\Scripts\Activate.ps1

3️⃣ Install dependencies
pip install customtkinter langchain langchain-ollama ollama
4️⃣ Install and run Ollama

Download Ollama from: https://ollama.com

Then run:

ollama pull phi3
ollama serve

▶️ Run the Application
python chatbot_langchain_gui.py
