import pandas as pd

data_csv=pd.read_csv("nato_phonetic_alphabet.csv")

data_dict={row.letter : row.code for (index,row) in data_csv.iterrows()}
#print(data_dict)

name=input("Enter a string: ")

name_list=[data_dict[char.upper()] for char in name ]

print(name_list)