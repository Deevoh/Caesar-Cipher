alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

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

encrypt(text)