import customtkinter as ctk
from langchain_ollama import OllamaLLM
import threading
import json
import os

# ====== MODEL ======
llm = OllamaLLM(model="phi3")

# ====== SETTINGS ======
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

HISTORY_FILE = "chat_history.json"

# ====== LOAD HISTORY ======
messages = []

if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        messages = json.load(f)

# ====== SAVE HISTORY ======
def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)

# ====== APP ======
app = ctk.CTk()
app.title("LangChain AI Chatbot (Phi-3)")
app.geometry("520x650")

# ====== CHAT FRAME ======
chat_frame = ctk.CTkScrollableFrame(app)
chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

# ====== ADD MESSAGE ======
def add_message(text, sender):
    container = ctk.CTkFrame(chat_frame, fg_color="transparent")

    if sender == "user":
        bubble = ctk.CTkLabel(
            container,
            text=text,
            fg_color="#2E7D32",
            text_color="white",
            corner_radius=12,
            padx=12,
            pady=8,
            wraplength=320,
            justify="left"
        )
        bubble.pack(anchor="e", padx=(80, 10), pady=5)

    else:
        bubble = ctk.CTkLabel(
            container,
            text=text,
            fg_color="#3A3A3A",
            text_color="white",
            corner_radius=12,
            padx=12,
            pady=8,
            wraplength=320,
            justify="left"
        )
        bubble.pack(anchor="w", padx=(10, 80), pady=5)

    container.pack(fill="x")
    app.after(100, lambda: chat_frame._parent_canvas.yview_moveto(1.0))

# ====== RESPONSE HANDLER ======
def generate_response(user_input, typing_label):
    try:
        # Basic context: last 5 messages
        context = "\n".join(messages[-5:])
        prompt = f"{context}\nUser: {user_input}\nAI:"

        response = llm.invoke(prompt)

        messages.append(f"User: {user_input}")
        messages.append(f"AI: {response}")

        save_history()

        app.after(0, lambda: show_response(response, typing_label))

    except Exception as e:
        app.after(0, lambda: show_response("Error: " + str(e), typing_label))


def show_response(response, typing_label):
    typing_label.destroy()
    add_message(response, "bot")

    # Re-enable send button
    send_btn.configure(state="normal")

# ====== SEND MESSAGE ======
def send_message():
    user_input = entry.get().strip()
    if not user_input:
        return

    entry.delete(0, "end")

    add_message(user_input, "user")

    # Disable send button while waiting for response
    send_btn.configure(state="disabled")

    typing_label = ctk.CTkLabel(chat_frame, text="Bot is typing...", text_color="gray")
    typing_label.pack(anchor="w", padx=10)

    threading.Thread(target=generate_response, args=(user_input, typing_label)).start()
# ====== INPUT AREA ======
bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(fill="x", padx=10, pady=10)

entry = ctk.CTkEntry(bottom_frame, placeholder_text="Type a message...")
entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

send_btn = ctk.CTkButton(bottom_frame, text="Send", command=send_message)
send_btn.pack(side="right", padx=(5, 10), pady=10)

app.bind("<Return>", lambda event: send_message())

# ====== RUN ======
app.mainloop()