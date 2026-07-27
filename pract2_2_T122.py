import tkinter as tk
from tkinter import messagebox
import math

# ---------------------------
# Functions
# ---------------------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


def encrypt(message, e, n):
    return [pow(ord(ch), e, n) for ch in message]


def decrypt(cipher, d, n):
    return ''.join(chr(pow(c, d, n)) for c in cipher)


# ---------------------------
# Generate Keys
# ---------------------------

def generate_keys():
    try:
        p = int(p_entry.get())
        q = int(q_entry.get())
        e = int(e_entry.get())

        if not (is_prime(p) and is_prime(q)):
            messagebox.showerror("Error", "p and q must be prime.")
            return

        n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(e, phi) != 1:
            messagebox.showerror("Error", "e must be coprime with φ(n).")
            return

        d = mod_inverse(e, phi)

        public_key.config(text=f"Public Key : ({e}, {n})")
        private_key.config(text=f"Private Key : ({d}, {n})")

        root.n = n
        root.e = e
        root.d = d

    except:
        messagebox.showerror("Error", "Enter valid values.")


# ---------------------------
# Encrypt
# ---------------------------

def encrypt_message():
    try:
        message = message_entry.get()

        cipher = encrypt(message, root.e, root.n)

        cipher_entry.delete(0, tk.END)
        cipher_entry.insert(0, " ".join(map(str, cipher)))

    except:
        messagebox.showerror("Error", "Generate Keys First.")


# ---------------------------
# Decrypt
# ---------------------------

def decrypt_message():
    try:
        cipher = list(map(int, cipher_entry.get().split()))

        plain = decrypt(cipher, root.d, root.n)

        decrypted.config(text="Decrypted Message : " + plain)

    except:
        messagebox.showerror("Error", "Invalid Cipher Text.")


# ---------------------------
# GUI
# ---------------------------

root = tk.Tk()
root.title("RSA Algorithm")
root.geometry("650x550")
root.configure(bg="#EAF4FC")

tk.Label(root, text="RSA Encryption & Decryption",
         font=("Arial",18,"bold"),
         bg="#EAF4FC",
         fg="navy").pack(pady=10)

tk.Label(root,text="Prime Number p",bg="#EAF4FC").pack()
p_entry=tk.Entry(root,width=30)
p_entry.pack()

tk.Label(root,text="Prime Number q",bg="#EAF4FC").pack()
q_entry=tk.Entry(root,width=30)
q_entry.pack()

tk.Label(root,text="Public Key e",bg="#EAF4FC").pack()
e_entry=tk.Entry(root,width=30)
e_entry.pack()

tk.Button(root,text="Generate Keys",
          command=generate_keys,
          bg="green",
          fg="white",
          width=20).pack(pady=10)

public_key=tk.Label(root,text="",bg="#EAF4FC",font=("Arial",11,"bold"))
public_key.pack()

private_key=tk.Label(root,text="",bg="#EAF4FC",font=("Arial",11,"bold"))
private_key.pack()

tk.Label(root,text="Message",bg="#EAF4FC").pack(pady=5)

message_entry=tk.Entry(root,width=50)
message_entry.pack()

tk.Button(root,text="Encrypt",
          command=encrypt_message,
          bg="blue",
          fg="white",
          width=15).pack(pady=8)

tk.Label(root,text="Cipher Text",bg="#EAF4FC").pack()

cipher_entry=tk.Entry(root,width=60)
cipher_entry.pack()

tk.Button(root,text="Decrypt",
          command=decrypt_message,
          bg="orange",
          fg="white",
          width=15).pack(pady=8)

decrypted=tk.Label(root,text="",font=("Arial",12,"bold"),bg="#EAF4FC")
decrypted.pack(pady=10)

root.mainloop()
