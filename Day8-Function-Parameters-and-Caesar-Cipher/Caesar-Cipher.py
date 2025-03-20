
from caesar_cipher_logo import logo
print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position + shift) % len(alphabets)
            encrypted_text += alphabets[new_position]
        else:
            encrypted_text += letter
    print(f"The encoded text is {encrypted_text}")

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position - shift) % len(alphabets)
            decrypted_text += alphabets[new_position]
        else:
            decrypted_text += letter
    print(f"The decoded text is {decrypted_text}")

def caesar(text, shift, encode_decode):
    if encode_decode == "decode":
        shift *= -1
    output_text = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position + shift) % len(alphabets)
            output_text += alphabets[new_position]
        else:
            output_text += letter
    print(f"The {encode_decode}d text is {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        caesar(text, shift, "encode")
    elif direction == "decode":
        caesar(text, shift, "decode")
    else:
        print("Invalid input")
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False