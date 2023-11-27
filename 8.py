def decrypt_affine_cipher(ciphertext, a, b):
    m = 26  # size of the alphabet

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()

            # Calculate modular multiplicative inverse of a (mod m)
            a_inv = mod_inverse(a, m)

            # Decryption formula: P = a^(-1)(C - b) mod m
            decrypted_char = chr((a_inv * (ord(char) - ord('A') - b)) % m + ord('A'))

            plaintext += decrypted_char if is_upper else decrypted_char.lower()
        else:
            plaintext += char

    return plaintext

def main():
    ciphertext = input("Enter the ciphertext: ")
    
    # Assuming "B" corresponds to the most frequent letter and "U" corresponds to the second most frequent
    most_frequent = "B"
    second_most_frequent = "U"

    # Calculate the key coefficients a and b
    a = (ord(most_frequent) - ord(second_most_frequent)) % 26
    b = (ord(most_frequent) - ord('A')) % 26

    plaintext = decrypt_affine_cipher(ciphertext, a, b)
    print("Decrypted Text:", plaintext)

if __name__ == "__main__":
    main()
