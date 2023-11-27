def generate_vigenere_table():
    table = [[chr((i + j) % 26 + ord('A')) for j in range(26)] for i in range(26)]
    return table

def encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    table = generate_vigenere_table()

    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            key_char = key[i % len(key)]
            row = ord(key_char) - ord('A')
            col = ord(char) - ord('A')
            ciphertext += table[row][col]
        else:
            ciphertext += char

    return ciphertext

def main():
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    ciphertext = encrypt(plaintext, key)
    print("Encrypted Text:", ciphertext)

if __name__ == "__main__":
    main()
