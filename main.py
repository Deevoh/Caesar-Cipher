alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text):
    listed_input = list(text)
    index_values = []
    encrypted_wrapped = []
    for char in listed_input:
        index = alphabet.index(char)
        index_values.append(index)
    shifted_index = [num + shift for num in index_values]
    for index in shifted_index:
        if index >= 0 and index < len(alphabet):
            encrypted_wrapped.append(alphabet[index])
        else:
            wrapped_index = index % len(alphabet)
            encrypted_wrapped.append(alphabet[wrapped_index])
    encrypted = ''.join(encrypted_wrapped)
    print(f"The encoded word is: {encrypted}")

def decrypt(text):
    listed_input2 = list(text)
    index2_values = []
    decrypted_wrapped = []
    for char in listed_input2:
        index2 = alphabet.index(char)
        index2_values.append(index2)
    shifted_index2 = [num - shift for num in index2_values]
    for index in shifted_index2:
        if index >= 0 and index < len(alphabet):
            decrypted_wrapped.append(alphabet[index])
        else:
            wrapped_index2 = index % len(alphabet)
            decrypted_wrapped.append(alphabet[wrapped_index2])
    decrypted = ''.join(decrypted_wrapped)
    print(f"The decoded word is: {decrypted}")

while True:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(text)
            break
        if direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypt(text)
        else:
            print("Invalid input.")
        break