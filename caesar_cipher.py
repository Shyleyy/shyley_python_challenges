def caesar_cipher(text, shift):
    result = ""

    for letter in text:
        if letter.isalpha():
            start = ord('A') if letter.isupper() else ord('a')
      
            shifted = (ord(letter) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += letter  

    return result

input_text = input("Enter text to encrypt: ")
shift_value = int(input("Enter shift value: "))
encrypted_text = caesar_cipher(input_text, shift_value)
print(f"Encrypted text: {encrypted_text}")