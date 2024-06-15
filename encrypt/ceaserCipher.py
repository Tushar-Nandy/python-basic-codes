from asciiart import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=len(alphabet)
punctuation=[',','.',' ','!','$','"',"'","(",')','1','2','3','4','5','6','7','8','9','0','-','_','/','@','?']
def caser(shift,letter,opr):
    text=''
    if opr=="decrypt":
        shift*=-1
    for word in letter:
        if word in punctuation:
            text+=word
        else:
            index=alphabet.index(word)+shift
            if index>=0:
                index=index%n
            text+=alphabet[index]
    print(f"The {opr}ed word is: {text}")


def main():
    shift=int(input("Enter the encoding (shifting) number: "))
    letter=input("Enter the message: ").lower()
    operation=input("What you want to do encrypt or decrypt: ").lower()
    if operation !='decrypt' and operation !="encrypt":
        print("Invalid operation")
    else:
        caser(shift,letter,operation)
main()