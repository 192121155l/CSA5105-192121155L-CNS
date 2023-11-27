def generate_key_square(key):
    key_square = [['' for _ in range(5)] for _ in range(5)]
    key = key.replace('J', 'I')
    key += 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    index = 0
    for i in range(5):
        for j in range(5):
            key_square[i][j] = key[index]
            index += 1
    
    return key_square

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    key_square = generate_key_square(key)
    plaintext = plaintext.replace('J', 'I')
    plaintext_pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

    encrypted_text = ""

    for pair in plaintext_pairs:
        row1, col1 = find_position(key_square, pair[0])
        row2, col2 = find_position(key_square, pair[1])

        if row1 == row2:
            encrypted_text += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_square[row1][col2] + key_square[row2][col1]

    return encrypted_text

def main():
    key = input("Enter the key: ").upper()
    plaintext = input("Enter the plaintext: ").upper()

    encrypted_text = playfair_encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()
