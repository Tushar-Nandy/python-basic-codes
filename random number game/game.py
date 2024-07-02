from art import logo
import random
import os

play=False

def createRandomNumber():
    return random.randint(1,100)
def chances(mode):
    global chance
    if mode=='d':
        return 5
    else:
        return 10

def want_to_play():
    global play
    ans=input("Do you want to play?\nEnter 'y' for Yes and 'n' for No: ").lower()
    if ans=='y':
        play=True
    else:
        play=False
def take_a_guess():
    guess=int(input("Enter a number between 1 and 100: "))
    return guess

def game():
    target=createRandomNumber()
    guess=-99999
    print(logo)
    createRandomNumber()
    mode=input("Which mode do you want to play? \nEnter 'd' for difficult and 'e' for easy: ").lower()
    chance=chances(mode)
    while chance!=0:
        guess=take_a_guess()
        chance-=1
        if guess==target:
            print("You win!! 😁🥳🤩")
            break
        else:
            if guess>target:
                print("Your guess is high")
            else:
                print("Your guess is low")
            print(f"{chance} remaining")
    if chance==0 and guess!=target:
        print(f"You loss 🥲\nThe number was {target}")

want_to_play()
while play:
    game()
    want_to_play()
    os.system('cls')

