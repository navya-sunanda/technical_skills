import tkinter as tk
from tkinter import scrolledtext

# DATASET
dataset = {
    "hi": "Hello! 😊",
    "hello": "Hi there! 👋",
    "how are you": "I'm doing great! What about you?",
    "what is your name": "I am Navya Chatbot 🤖🔥",
    "python": "Python is a powerful programming language.",
    "ai": "AI means Artificial Intelligence.",
    "what is computer": "Computer is an electronic machine.",
    "what is internet": "Internet connects the world 🌍",
    "tell me a joke": "Why did Python laugh? Because it saw a bug 😄",
    "machine learning": "It is a way for computers to learn from data.",
    "java": "Java is used for Android applications 🤖",
    "who created you": "I was created using Python 😊",
    "nlp": "NLP means Natural Language Processing.",
    "chatbot": "A chatbot is a program that talks with users.",
    "joke": "Why did the computer sleep? Because it was tired 😄",
    "internet": "Internet connects the whole world 🌍",
    "bye": "Goodbye! Take care 💖"
}

# RESPONSE FUNCTION
def get_response(user_input):
    user_input = user_input.lower()

    for key in dataset:
        if key in user_input:
            return dataset[key]

    return "Sorry, I don't understand. Try something else!"

# SEND MESSAGE FUNCTION
def send_message():
    user_input = entry.get().strip()

    if user_input == "":
        return

    chatbox.insert(tk.END, "You: " + user_input + "\n")

    response = get_response(user_input)

    chatbox.insert(tk.END, "Navya Bot: " + response + "\n\n")

    chatbox.see(tk.END)

    entry.delete(0, tk.END)

# GUI WINDOW
root = tk.Tk()
root.title("Navya Chatbot 🤖")

# CHATBOX
chatbox = scrolledtext.ScrolledText(
    root,
    width=50,
    height=20,
    bg="black",
    fg="white",
    font=("Arial", 12)
)

chatbox.pack(padx=10, pady=10)

# WELCOME MESSAGE
chatbox.insert(tk.END, "Navya Bot: Hello! I am Navya Chatbot 🤖\n\n")

# ENTRY BOX
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# SEND BUTTON
send_btn = tk.Button(
    root,
    text="Send",
    command=send_message,
    font=("Arial", 12),
    bg="blue",
    fg="white"
)

send_btn.pack(pady=5)

# ENTER KEY SUPPORT
entry.bind("<Return>", lambda event: send_message())

# RUN WINDOW
root.mainloop()