def caesar_cipher(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26 + ord('A' if char.isupper() else 'a'))
            result += shifted_char
        else:
            result += char

    return result

def main():
    message = input("Enter the message: ")  
    for shift in range(1, 26):
        ciphered_message = caesar_cipher(message, shift)
        print(f"Shift {shift}: {ciphered_message}")

if __name__ == "__main__":
    main()
``
