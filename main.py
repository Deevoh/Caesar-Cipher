import os
from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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
    print(f"\nThe encoded word is: \n{encrypted}")

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
    print(f"\nThe decoded word is: \n{decrypted}")

def input_encrypt():
    text = input("\nType your message:\n").lower()
    while True:
        shift_input = input("\nType the shift number:\n")
        if shift_input.isdigit():
            shift = int(shift_input)
            encrypt(text, shift)
            break
        else:
            print("Invalid input. Please use numbers only.")
            continue

def input_decrypt():
    text = input("\nType your message:\n").lower()
    while True:
        shift_input = input("\nType the shift number:\n")
        if shift_input.isdigit():
            shift = int(shift_input)
            decrypt(text, shift)
            break
        else:
            print("Invalid input. Please use numbers only.")
            continue


while True:
    while True:
        print(logo)
        while True:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            end = False
            if direction == "encode":
                input_encrypt()
                end = True
            elif direction == "decode":
                input_decrypt()
                end = True
            else:
                print("Invalid input.\n")
                continue
            while True:
                if end:
                    go_again = input("\nDo you want another cipher? (y/n): ").lower()
                    if go_again == "y":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    elif go_again == "n":
                        print("\nGoodbye.\n")
                        exit()
                    else:
                        print("Invalid input. 'y' or 'n' only.")
                        continue
            break