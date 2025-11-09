# Caesar-cipher
A Python-based GUI tool built with Tkinter to encrypt and decrypt messages using the Caesar Cipher technique. Features include a user-friendly interface, shift value customization, real-time status updates, and clipboard support — ideal for learning basic cryptography.

🧭 Overview

The Caesar Cipher Encryption Tool helps users visualize how text messages can be securely encoded and decoded using a shift-based substitution cipher.
It’s an educational project designed to demonstrate the principles of encryption, decryption, and data confidentiality in a simple and interactive way.

⚙️ How the Caesar Cipher Works

The Caesar Cipher shifts each letter in the message by a fixed number of positions in the alphabet.
For example, with a shift of 3:

A → D

B → E

C → F

To decrypt, the process is simply reversed by shifting in the opposite direction.

Formula:

Encryption: C = (P + K) mod 26  
Decryption: P = (C - K) mod 26


Where:

C = Encrypted character

P = Plain character

K = Shift key

✨ Key Features

🧩 Encrypt and Decrypt messages easily

🧠 Customizable shift value (1–25)

🖥️ Graphical interface built with Tkinter

⚡ Copy to clipboard functionality

✅ Real-time status updates

🚫 Error handling for invalid inputs

💡 Usage Example
Encrypting a Message

Input Message: HELLO
Shift Value: 3
Encrypted Output: KHOOR

Decrypting a Message

Input Message: KHOOR
Shift Value: 3
Decrypted Output: HELLO

🧰 Implementation Details

Language: Python

Libraries Used:

tkinter → for GUI design

messagebox → for alert dialogs

Core Logic: Uses ASCII values and modular arithmetic for alphabet shifting.

Design Theme: Dark-mode GUI with enhanced visual feedback.

🚀 How to Run the Tool

Clone the Repository

git clone https://github.com/yourusername/Caesar-Cipher-Encryption-Tool.git
cd Caesar-Cipher-Encryption-Tool


Run the Program

python caesar_cipher_tool.py


Enter:

Your message

Shift value (1–25)

Choose “Encrypt” or “Decrypt”

View the output directly in the GUI or copy it to clipboard.

🏁 Conclusion

The Caesar Cipher Encryption Tool is a beginner-friendly Python project that demonstrates the fundamentals of classical cryptography and GUI programming.
It’s a great starting point for those learning about encryption algorithms, Python development, and user interface design.
