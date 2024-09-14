import pandas as pd

data_csv=pd.read_csv("nato_phonetic_alphabet.csv")
is_on=True
data_dict={row.letter : row.code for (index,row) in data_csv.iterrows()}
#print(data_dict)

while is_on:
    name=input("Enter a string: ")
    try:
        name_list=[data_dict[char.upper()] for char in name ]
    except:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_on=False
print(name_list)