alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=len(alphabet)
punctuation=[',','.',' ','!','$','"',"'","(",')','1','2','3','4','5','6','7','8','9','0','-','_','/','@']
def encrypt(shift,letter):    
    encodeLetter=''
    for word in letter:
        if word in punctuation:
            encodeLetter+=word
        else:
            encodeLetter+=alphabet[(alphabet.index(word)+shift)%n]
    print(f"The encoded message is {encodeLetter}")

def decrypt(shift,letter):
    decode=''
    for word in letter:
        if word in punctuation:
            decode+=word
        else:
            index=alphabet.index(word)-shift
            if index>=0:
                decode+=alphabet[index]
            else:
                decode+=alphabet[index+n]
    print(f"The decoded message is {decode}")

def main():
    shift=int(input("Enter the encoding (shifting) number: "))
    letter=input("Enter the message: ").lower()
    operation=input("What you want to do encrypt(e) or decrypt(d): ").lower()
    if operation=='e':
        encrypt(shift,letter)
    elif operation=='d':
        decrypt(shift,letter)
    else:
        print("Invalid operation")
main()