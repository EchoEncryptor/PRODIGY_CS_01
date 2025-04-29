# Caesar Cipher – Encryption & Decryption Tool

## 📜 Description

This Python script implements a simple **Caesar Cipher** encryption and decryption tool. The Caesar Cipher is one of the earliest and simplest forms of encryption, where each letter in the plaintext is shifted a fixed number of positions in the alphabet. This script supports both encryption and decryption with customizable shift values and preserves the original case of letters. Non-alphabetic characters remain unchanged, making it suitable for encrypting full sentences, including punctuation.

---

## 🚀 Features

- Encrypt or decrypt any message using Caesar Cipher
- Case-sensitive character handling
- Keeps non-alphabetic characters unchanged (spaces, punctuation, numbers, etc.)
- Input validation for correct user interaction

---

## 🛠️ Usage

### ✅ Requirements
- Python 3.x

### ▶️ Run the Program

You can run the script via command line:

```bash
python caesar_cipher.py
```

### 🔧 Example Interaction

```
=== Caesar Cipher ===
Do you want to (E)ncrypt or (D)ecrypt? E
Enter your message: Hello, World!
Enter shift value (0-25): 3
Encrypted message: Khoor, Zruog!
```

```
=== Caesar Cipher ===
Do you want to (E)ncrypt or (D)ecrypt? D
Enter your message: Khoor, Zruog!
Enter shift value (0-25): 3
Decrypted message: Hello, World!
```

---

## 📂 File Structure

```
caesar_cipher.py      # Main script for Caesar Cipher encryption and decryption
```

---

## 📌 Notes

- Only alphabetic characters are shifted.
- Characters like numbers, punctuation, and spaces are not altered.
- Shift values outside the 0-25 range are automatically wrapped using modulo.

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

Let me know if you want the `LICENSE` file or a graphical user interface (GUI) added to the tool.
