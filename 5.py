def decrypt_simple_substitution(ciphertext):
    frequency = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, ')': 0, '(': 0, '*': 0, ';': 0, ':': 0, '—': 0, ']': 0, '[': 0, '†': 0, '¶': 0, '‡': 0}

    for char in ciphertext:
        if char in frequency:
            frequency[char] += 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    most_common = ''.join([char for char, _ in sorted_frequency])

    decryption_key = {}
    for i in range(len(most_common)):
        decryption_key[most_common[i]] = chr(ord('A') + i)

    decrypted_text = ''.join([decryption_key[char] if char in decryption_key else char for char in ciphertext])
    return decrypted_text

def main():
    ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡8†83 (88)5†;46(;88*96*?;8)‡(;485);5†2:‡(;4956*2(5—4)8¶8* ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
    
    decrypted_text = decrypt_simple_substitution(ciphertext)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
