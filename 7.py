import string

def decrypt_additive_cipher(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = decrypt_char(char, key)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def decrypt_char(char, key):
    if char.islower():
        return chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
    elif char.isupper():
        return chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
    else:
        return char

def letter_frequency_attack(ciphertext, num_results=10):
    frequencies = {char: 0 for char in string.ascii_uppercase}
    
    for char in ciphertext:
        if char.isalpha():
            frequencies[char.upper()] += 1

    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    
    top_guesses = []
    for _, key_char in sorted_frequencies[:num_results]:
        key = (ord(key_char) - ord('E')) % 26
        plaintext_guess = decrypt_additive_cipher(ciphertext, key)
        top_guesses.append((key, plaintext_guess))
    
    return top_guesses

def main():
    ciphertext = input("Enter the ciphertext: ")
    num_results = int(input("Enter the number of top plaintext guesses to display: "))

    guesses = letter_frequency_attack(ciphertext, num_results)
    
    print("\nTop {} Possible Plaintexts:".format(num_results))
    for i, (key, guess) in enumerate(guesses, start=1):
        print("{}. Key: {}, Plaintext: {}".format(i, key, guess))

if __name__ == "__main__":
    main()
