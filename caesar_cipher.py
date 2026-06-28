def caesar_cipher(text, shift, mode):
    result = ""
    symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    sym_len = len(symbols)  # 32 symbols

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char

        elif char.isdigit():
            if mode == "encrypt":
                new_char = str((int(char) + shift) % 10)
            else:
                new_char = str((int(char) - shift) % 10)
            result += new_char

        elif char in symbols:
            idx = symbols.index(char)
            if mode == "encrypt":
                new_char = symbols[(idx + shift) % sym_len]
            else:
                new_char = symbols[(idx - shift) % sym_len]
            result += new_char

        else:
            result += char  # spaces unchanged

    return result


# ── Main Program ──
print("===== Caesar Cipher =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("\nChoose (1/2): ").strip()

if choice == "1":
    mode = "encrypt"
elif choice == "2":
    mode = "decrypt"
else:
    print("Invalid choice!")
    exit()

message = input("Enter your message: ")
shift   = int(input("Enter shift value (1-25): "))

output = caesar_cipher(message, shift, mode)
print(f"\nResult: {output}")