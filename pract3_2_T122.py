import tkinter as tk
from tkinter import messagebox
import hmac
import hashlib


def generate_mac():
    message = message_entry.get("1.0", tk.END).strip()
    secret_key = key_entry.get().strip()

    if not message or not secret_key:
        messagebox.showerror("Error", "Please enter both Message and Secret Key.")
        return

    mac = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    mac_entry.delete(0, tk.END)
    mac_entry.insert(0, mac)



def verify_mac():
    message = message_entry.get("1.0", tk.END).strip()
    secret_key = key_entry.get().strip()
    received_mac = verify_entry.get().strip()

    if not message or not secret_key or not received_mac:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    generated_mac = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(generated_mac, received_mac):
        result_label.config(
            text="✔ MAC Verified Successfully!\nData Integrity & Authenticity Confirmed.",
            fg="green"
        )
    else:
        result_label.config(
            text="✖ MAC Verification Failed!\nMessage or Key is Incorrect.",
            fg="red"
        )


root = tk.Tk()
root.title("Message Authentication Code (MAC)")
root.geometry("600x500")
root.configure(bg="#F8B2B2")

title = tk.Label(
    root,
    text="Message Authentication Code (MAC)",
    font=("Arial", 18, "bold"),
    bg="#F8B2B2",
    fg="#8B639B"
)
title.pack(pady=15)

tk.Label(root, text="Enter Message:", font=("Arial", 12),
         bg="#F8B2B2").pack(anchor="w", padx=20)

message_entry = tk.Text(root, height=5, width=60)
message_entry.pack(padx=20, pady=5)

tk.Label(root, text="Secret Key:", font=("Arial", 12),
         bg="#F8B2B2").pack(anchor="w", padx=20)

key_entry = tk.Entry(root, width=50, show="*")
key_entry.pack(padx=20, pady=5)

generate_btn = tk.Button(
    root,
    text="Generate MAC",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=generate_mac
)
generate_btn.pack(pady=10)

tk.Label(root, text="Generated MAC:", font=("Arial", 12),
         bg="#F8B2B2").pack(anchor="w", padx=20)

mac_entry = tk.Entry(root, width=80)
mac_entry.pack(padx=20, pady=5)

tk.Label(root, text="Enter MAC to Verify:", font=("Arial", 12),
         bg="#F8B2B2").pack(anchor="w", padx=20)

verify_entry = tk.Entry(root, width=80)
verify_entry.pack(padx=20, pady=5)

verify_btn = tk.Button(
    root,
    text="Verify MAC",
    font=("Arial", 12, "bold"),
    bg="#403D88",
    fg="white",
    command=verify_mac
)
verify_btn.pack(pady=15)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#F8B2B2"
)
result_label.pack(pady=10)

root.mainloop()
