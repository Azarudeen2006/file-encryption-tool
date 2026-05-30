import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Load key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

def encrypt_file():
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted)

    messagebox.showinfo("Success", "File Encrypted Successfully!")

def decrypt_file():
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    with open(file_path, "rb") as file:
        data = file.read()

    decrypted = fernet.decrypt(data)

    with open(file_path, "wb") as file:
        file.write(decrypted)

    messagebox.showinfo("Success", "File Decrypted Successfully!")

# Main Window
root = tk.Tk()
root.title("File Encryption Tool")
root.geometry("400x250")

title = tk.Label(root, text="File Encryption Tool", font=("Arial", 16, "bold"))
title.pack(pady=20)

encrypt_btn = tk.Button(root, text="Encrypt File", command=encrypt_file, width=20)
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(root, text="Decrypt File", command=decrypt_file, width=20)
decrypt_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.quit, width=20)
exit_btn.pack(pady=10)

root.mainloop()