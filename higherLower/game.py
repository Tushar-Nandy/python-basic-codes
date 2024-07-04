from logic import data
from art import logo, vs
import random
import os

play=True
textA=""
textB=""
valueA=0
valueB=0
text=""
value=0
def begin():
    global textA, textB,valueA,valueB
    for _ in range(2):
        n=len(data)
        index=random.randint(0,n)
        name,follower_count,description,country=data[index].values()
        if textA=="":
            textA=f"{name} is a {description} in {country}"
            valueA=follower_count
        else:
            textB=f"{name} is a {description} in {country}"
            valueB=follower_count
        data.remove(data[index])    

def continue_game():
    global text,value
    n=len(data)
    index=random.randint(0,n)
    name,follower_count,description,country=data[index].values()
    text=f"{name} is a {description} in {country}"
    value=follower_count
    data.remove(data[index])

def playGame():
    score=0
    global textB,textA,valueA,valueB,play
    begin()
    while play:
        print(logo)
        print(f"Welcome to the Higher and Lower game. Your score is {score}")
        print(f"Text A: {textA}")
        print(vs)
        print(f"Text B: {textB}")
        print()
        choice=input("Which among the two has a higher follower count, 'a' for Text A and 'b'' for Text B: ").lower()
        if choice=='a':
            if valueA>valueB:
                continue_game()
                textB=text
                valueB=value
                score+=1
            else:
                play=False

        elif choice=='b':
            if valueA<valueB:
                continue_game()
                textA=text
                valueA=value
                score+=1
            else:
                play=False
        if len(data)<2:
            break
    os.system('cls')
    print(logo)
    print(f"Thank you for playing. Your score is: {score}")

playGame()