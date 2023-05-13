import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end = False

def encrypt(text, shift):
    encrypted_wrapped = []
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            shifted_index = (index + shift) % len(alphabet)
            shifted_chars = alphabet[shifted_index]
            encrypted_wrapped.append(shifted_chars)
        else:
            encrypted_wrapped.append(char)
    encrypted = ''.join(encrypted_wrapped)
    print(f"The encoded word is: {encrypted}")
    end = True

def decrypt(text, shift):
    decrypted_wrapped = []
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            shifted_index = (index - shift) % len(alphabet)
            shifted_chars = alphabet[shifted_index]
            decrypted_wrapped.append(shifted_chars)
        else:
            decrypted_wrapped.append(char)
    decrypted = ''.join(decrypted_wrapped)
    print(f"The decoded word is: {decrypted}")

print(logo)
while True:
    while True:
        while True:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            if direction == "encode":
                text = input("Type your message:\n").lower()
                shift = int(input("Type the shift number:\n"))
                encrypt(text, shift)
                end = True
            if direction == "decode":
                text = input("Type your message:\n").lower()
                shift = int(input("Type the shift number:\n"))
                decrypt(text, shift)
                end = True
            else:
                print("Invalid input.")
            break
        if end:
            go_again = input("Do you want another cipher? (y/n): ").lower()
            if go_again == "y":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif go_again == "n":
                print("Goodbye.")
                exit()
            else:
                print("Invalid input.")
                continue