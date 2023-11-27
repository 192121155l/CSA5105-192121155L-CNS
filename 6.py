import random

def generate_key(length):
    return [random.randint(0, 25) for _ in range(length)]

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
    plaintext = input("Enter the plaintext: ")
    key_length = len(plaintext)
    key = generate_key(key_length)

    ciphertext = vigenere_encrypt(plaintext, key)
    print("Key:", key)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
