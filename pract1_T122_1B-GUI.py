import tkinter as tk
from tkinter import messagebox


def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    result = ""

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0

    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        result += rail[row][col]
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return result


def encrypt_gui():
    text = message.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Enter a message")
        return

    try:
        key = int(key_entry.get())
        if key < 2:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter a valid rail number (>=2)")
        return

    result = encrypt(text, key)

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)
    output.config(state="disabled")


def decrypt_gui():
    text = message.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Enter a message")
        return

    try:
        key = int(key_entry.get())
        if key < 2:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter a valid rail number (>=2)")
        return

    result = decrypt(text, key)

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)
    output.config(state="disabled")


def clear():
    message.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.config(state="disabled")


root = tk.Tk()
root.title("Rail Fence Cipher")
root.geometry("520x470")
root.configure(bg="#FFB6A6")

title = tk.Label(root,
                 text="Rail Fence Cipher Encryption & Decryption",
                 font=("Arial", 16, "bold"),
                 bg="#FF84BA",
                 fg="navy")
title.pack(pady=10)

tk.Label(root,
         text="Enter Message",
         bg="#FF84BA",
         font=("Arial",11,"bold")).pack()

message = tk.Text(root,height=5,width=50)
message.pack()

tk.Label(root,
         text="Number of Rails",
         bg="#FF84BA",
         font=("Arial",11,"bold")).pack(pady=5)

key_entry = tk.Entry(root,font=("Arial",12),width=10)
key_entry.pack()

frame = tk.Frame(root,bg="#FF84BA")
frame.pack(pady=12)

tk.Button(frame,
          text="Encrypt",
          width=12,
          bg="green",
          fg="white",
          command=encrypt_gui).grid(row=0,column=0,padx=5)

tk.Button(frame,
          text="Decrypt",
          width=12,
          bg="blue",
          fg="white",
          command=decrypt_gui).grid(row=0,column=1,padx=5)

tk.Button(frame,
          text="Clear",
          width=12,
          bg="red",
          fg="white",
          command=clear).grid(row=0,column=2,padx=5)

tk.Label(root,
         text="Result",
         bg="#FF84BA",
         font=("Arial",11,"bold")).pack()

output = tk.Text(root,height=5,width=50,state="disabled")
output.pack(pady=5)

root.mainloop()
