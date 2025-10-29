import base64
import tkinter as tk
from tkinter import messagebox

def encode_text():
    text = entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    output.delete("1.0", tk.END)
    output.insert(tk.END, encoded)

def decode_text():
    text = entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter a Base64 code!")
        return
    try:
        decoded = base64.b64decode(text).decode("utf-8")
        output.delete("1.0", tk.END)
        output.insert(tk.END, decoded)
    except Exception:
        messagebox.showerror("Error", "Invalid Base64 code!")

root = tk.Tk()
root.title("Base64 Encoder / Decoder")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#2e2e2e")

tk.Label(root, text="Text / Code:", bg="#2e2e2e", fg="white", font=("Arial", 11)).pack(pady=5)
entry = tk.Text(root, height=7, width=55, bg="#1e1e1e", fg="white", insertbackground="white", wrap="word")
entry.pack(pady=5)

frame = tk.Frame(root, bg="#2e2e2e")
frame.pack(pady=10)
tk.Button(frame, text="Encode", command=encode_text, width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10)
tk.Button(frame, text="Decode", command=decode_text, width=15, bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)

tk.Label(root, text="Result:", bg="#2e2e2e", fg="white", font=("Arial", 11)).pack(pady=5)
output = tk.Text(root, height=7, width=55, bg="#1e1e1e", fg="white", insertbackground="white", wrap="word")
output.pack(pady=5)

root.mainloop()
