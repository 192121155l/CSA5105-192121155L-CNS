def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = key[i % len(key)]
            encrypted_char = encrypt_char(char, shift)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def encrypt_char(char, shift):
    if char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return char

def main():
    plaintext = "SENDMOREMONEY"
    key_stream = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

    ciphertext = vigenere_encrypt(plaintext, key_stream)
    print("Plaintext:", plaintext)
    print("Key Stream:", key_stream)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
