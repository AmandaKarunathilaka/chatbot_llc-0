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

- **Python** (Pycharm as IDE)
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
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
```
Activate it:
Windows:
```bash
.\.venv\Scripts\Activate.ps1
```
### 3️⃣ Install dependencies
```bash
pip install customtkinter langchain langchain-ollama ollama
```

### 4️⃣ Install and run Ollama

Download Ollama from: https://ollama.com

Then run:
```bash
ollama pull phi3
ollama serve
```
▶️ Run the Application
```bah
python chatbot_langchain_gui.py
```
OR just click on the run button on top navigation bar on the IDE.

🧠 How It Works
- Uses LangChain + Ollama to interact with the Phi-3 model
- Maintains conversation context using recent messages
- Stores chat history in a JSON file
- Displays messages using a modern GUI layout

📁 Project Structure

project-folder/
│
├── chat_history.json   # Stores conversation history
├── README.md           # Project documentation
├── main.py             # Main application file (chatbot GUI and logic)
└── .gitignore          # Files/folders to ignore in Git
