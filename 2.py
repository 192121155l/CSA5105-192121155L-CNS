def monoalphabetic_cipher(message, key):
    result = ""

    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            index = ord(char) - ord('A' if is_upper else 'a')
            substituted_char = key[index]
            substituted_char = substituted_char.upper() if is_upper else substituted_char.lower()

            result += substituted_char
        else:
            result += char

    return result
message = input("Enter the message: ")
key = input("Enter the substitution key (a permutation of the alphabet): ")
if len(key) == 26 and key.isalpha():
    substituted_message = monoalphabetic_cipher(message, key)
    print(f"Substituted message: {substituted_message}")
else:
    print("Invalid substitution key. Please enter a permutation of the alphabet.")
