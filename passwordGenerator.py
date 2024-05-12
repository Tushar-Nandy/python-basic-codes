#password generator
import random
password=[]
character=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol=special_characters = ['!','#','$','%','_','&','(',')','{','}','*','-','+','/','@','^']
number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
req=[]
print("welcome to password generator: ")
i=int(input("Enter number of alphabets in the password: "))
for _ in range(i):
    req.append('c')
i=int(input("Enter number of digits in the password: "))
for _ in range(i):
    req.append('d')
i=int(input("Enter number of symbols in the password: "))
for _ in range(i):
    req.append('s')
while len(req)!=0:
    w=random.choice(req)
    req.remove(w)
    if w=='c':
        password.append(random.choice(character))
    elif w=='d':
        password.append(random.choice(number))
    else:
        password.append(random.choice(symbol))

print(f"Password is: {''.join(password)}")