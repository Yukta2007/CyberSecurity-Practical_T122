import tkinter as tk
from tkinter import messagebox

def encrypt():
    text = message_entry.get("1.0", tk.END).strip()
    if text == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid numeric key.")
        return

    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    output_entry.config(state="normal")
    output_entry.delete("1.0", tk.END)
    output_entry.insert(tk.END, result)
    output_entry.config(state="disabled")


def decrypt():
    text = message_entry.get("1.0", tk.END).strip()
    if text == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid numeric key.")
        return

    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char

    output_entry.config(state="normal")
    output_entry.delete("1.0", tk.END)
    output_entry.insert(tk.END, result)
    output_entry.config(state="disabled")


def clear():
    message_entry.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)

    output_entry.config(state="normal")
    output_entry.delete("1.0", tk.END)
    output_entry.config(state="disabled")


root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x450")
root.configure(bg="#E8F0FE")

title = tk.Label(
    root,
    text="Caesar Cipher Encryption & Decryption",
    font=("Arial", 16, "bold"),
    bg="#E8F0FE",
    fg="navy"
)
title.pack(pady=10)

tk.Label(root, text="Enter Message:", bg="#E8F0FE",
         font=("Arial", 11, "bold")).pack()

message_entry = tk.Text(root, height=5, width=45)
message_entry.pack(pady=5)

tk.Label(root, text="Shift Key:", bg="#E8F0FE",
         font=("Arial", 11, "bold")).pack()

key_entry = tk.Entry(root, width=10, font=("Arial", 12))
key_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#E8F0FE")
button_frame.pack(pady=10)

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    width=12,
    bg="green",
    fg="white",
    command=encrypt
)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    width=12,
    bg="blue",
    fg="white",
    command=decrypt
)
decrypt_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    bg="red",
    fg="white",
    command=clear
)
clear_btn.grid(row=0, column=2, padx=5)

tk.Label(root, text="Result:", bg="#E8F0FE",
         font=("Arial", 11, "bold")).pack()

output_entry = tk.Text(root, height=5, width=45, state="disabled")
output_entry.pack(pady=5)

root.mainloop()
