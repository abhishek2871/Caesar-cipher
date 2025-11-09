import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Button Actions
def encrypt_text():
    message = entry_message.get()
    shift = entry_shift.get()

    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be a number!")
        return

    shift = int(shift)
    encrypted = caesar_cipher(message, shift, 'encrypt')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, encrypted)
    status_label.config(text="✅ Message Encrypted Successfully!", fg="#4CAF50")

def decrypt_text():
    message = entry_message.get()
    shift = entry_shift.get()

    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be a number!")
        return

    shift = int(shift)
    decrypted = caesar_cipher(message, shift, 'decrypt')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, decrypted)
    status_label.config(text="🔓 Message Decrypted Successfully!", fg="#2196F3")

def clear_all():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    output_text.delete(1.0, tk.END)
    status_label.config(text="")

def copy_to_clipboard():
    text = output_text.get(1.0, tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        status_label.config(text="📋 Output copied to clipboard!", fg="#FFD700")
    else:
        status_label.config(text="⚠️ Nothing to copy!", fg="orange")

# --- GUI Setup ---
root = tk.Tk()
root.title("Caesar Cipher Tool - Enhanced Edition")
root.geometry("480x400")
root.resizable(False, False)
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="🔐 Caesar Cipher Encryption Tool", bg="#1e1e2f", fg="#00FFFF", 
         font=("Helvetica", 15, "bold")).pack(pady=10)

# Message Input
tk.Label(root, text="Enter Message:", bg="#1e1e2f", fg="white", font=("Arial", 11)).pack(pady=5)
entry_message = tk.Entry(root, width=60)
entry_message.pack(pady=5)

# Shift Value
tk.Label(root, text="Enter Shift Value (1–25):", bg="#1e1e2f", fg="white", font=("Arial", 11)).pack(pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.pack(pady=5)

# Buttons
frame_buttons = tk.Frame(root, bg="#1e1e2f")
frame_buttons.pack(pady=15)

btn_encrypt = tk.Button(frame_buttons, text="Encrypt", command=encrypt_text, bg="#4CAF50", fg="white", width=12)
btn_encrypt.grid(row=0, column=0, padx=8)

btn_decrypt = tk.Button(frame_buttons, text="Decrypt", command=decrypt_text, bg="#2196F3", fg="white", width=12)
btn_decrypt.grid(row=0, column=1, padx=8)

btn_clear = tk.Button(frame_buttons, text="Clear", command=clear_all, bg="#F44336", fg="white", width=12)
btn_clear.grid(row=0, column=2, padx=8)

# Output Box
tk.Label(root, text="Output:", bg="#1e1e2f", fg="white", font=("Arial", 11)).pack(pady=5)
output_text = tk.Text(root, height=5, width=55, wrap="word", font=("Consolas", 10))
output_text.pack(pady=5)

# Copy Button
btn_copy = tk.Button(root, text="Copy", command=copy_to_clipboard, bg="#9C27B0", fg="white", width=10)
btn_copy.pack(pady=5)

# Status Label
status_label = tk.Label(root, text="", bg="#1e1e2f", fg="white", font=("Arial", 10, "italic"))
status_label.pack(pady=8)

root.mainloop()
