def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = key[i % len(key)]
            decrypted_char = decrypt_char(char, shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def decrypt_char(char, shift):
    if char.islower():
        return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    else:
        return char

def main():
    ciphertext = "KFAOMHDEDCYF"
    target_plaintext = "CASHNOTNEEDED"

    # Try different key streams until the decryption matches the target plaintext
    for i in range(26):
        key_stream = [i] * len(ciphertext)
        decrypted_text = vigenere_decrypt(ciphertext, key_stream)

        if decrypted_text.upper() == target_plaintext:
            print("Key Stream:", key_stream)
            print("Decrypted Text:", decrypted_text)
            break
    else:
        print("Key not found. Try a different approach or key length.")

if __name__ == "__main__":
    main()
