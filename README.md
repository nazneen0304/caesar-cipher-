# 🔐 Caesar Cipher — Python Implementation

A command-line Python program that encrypts and decrypts text using the **Caesar Cipher** algorithm. Built as part of a self-learning internship to explore cryptography fundamentals and Python string manipulation.

---

## 📌 What is Caesar Cipher?

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each character in a message by a fixed number of positions.

```
Plain text:   H E L L O
Shift by 3:   K H O O R
```

To decrypt, simply shift in the opposite direction.

---

## ✨ Features

- 🔡 Encrypts and decrypts **uppercase and lowercase letters** (A–Z, a–z)
- 🔢 Supports **digits** (0–9) with wrap-around
- 🔣 Supports **32 special symbols** (`! " # $ % & ...`)
- ♻️ Correct **wrap-around** using modulo arithmetic
- 💬 Spaces and unrecognized characters are preserved as-is
- 🖥️ Simple and clean **command-line interface**

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- No external libraries required

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/caesar-cipher.git

# Navigate into the project folder
cd caesar-cipher
```

### Running the program

```bash
python caesar_cipher.py
```

---

## 🖥️ Usage

```
===== Caesar Cipher =====
1. Encrypt
2. Decrypt

Choose (1/2): 1
Enter your message: Hello123!
Enter shift value (1-25): 3

Result: Khoor456$
```

---

## 🧠 How It Works

The program handles three types of characters differently:

| Character Type | Total Count | Wrap Using | Example (shift 3) |
|---|---|---|---|
| Letters (A–Z, a–z) | 26 | `% 26` | `A → D`, `Z → C` |
| Digits (0–9) | 10 | `% 10` | `7 → 0`, `9 → 2` |
| Symbols | 32 | `% 32` | `!→ $`, `~ → #` |

### Core logic

```python
# Encrypt a letter
new_char = chr((ord(char) - base + shift) % 26 + base)

# Decrypt a letter
new_char = chr((ord(char) - base - shift) % 26 + base)
```

- `ord()` converts a character to its ASCII number
- `chr()` converts a number back to a character
- `% 26` ensures wrap-around within the alphabet

---

## 📁 Project Structure

```
caesar-cipher/
│
├── caesar_cipher.py   # Main program
└── README.md          # Project documentation
```

---

## 📚 Concepts Learned

- ASCII values and `ord()` / `chr()` functions in Python
- Modulo arithmetic for character wrap-around
- Writing clean, reusable functions
- Handling edge cases (symbols, digits, negative modulo)
- Basic cryptography principles

---

## 🛡️ Limitations

- This is a basic educational cipher — **not suitable for real-world security**
- The Caesar Cipher is easily broken since there are only 25 possible shifts
- For real encryption, use modern algorithms like AES or RSA

---

## 👨‍💻 Author

**Your Name**
- GitHub: nazneen0304(https://github.com/nazneen0304)
- LinkedIn:Nazneen M(https://linkedin.com/in/Nazneen M)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with ❤️ as part of a self-learning internship journey.
