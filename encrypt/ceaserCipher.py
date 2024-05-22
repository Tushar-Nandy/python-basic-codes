alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=len(alphabet)
shift=int(input("Enter the encoding (shifting) number: "))
letter=input("Enter the message: ").lower()
encodeLetter=''
for word in letter:
    encodeLetter+=alphabet[alphabet.index(word)+shift]

print(f"The encoded message is {encodeLetter}")

