alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

index_values = ""

def encrypt(text):
    listed_string = list(text)
    index_values = []
    print(listed_string) # DEBUG
    for char in listed_string:
        index = alphabet.index(char)
        index_values.append(index)
    print(index_values)

encrypt(text)