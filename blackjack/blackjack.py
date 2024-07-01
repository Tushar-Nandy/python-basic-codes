from art import logo
import random
import os
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
n=len(cards)
play=False
playerCard=[]
computerCard=[]

def want_to_play():
    global playerCard
    global computerCard
    computerCard=[]
    playerCard=[]
    global play
    choice=input("Want to play a game of blackjack, 'y' for Yes and 'n' for No: ").lower()
    if choice=='y':
        play=True
    else:
        play=False

def distribute_card():
    for _ in range(2):
        computerCard.append(cards[(random.randint(1,100)%n)])
        playerCard.append(cards[(random.randint(1,100)%n)])

def show_card():
    playerScore=0
    for i in range(len(playerCard)):
        playerScore+=playerCard[i]
    print(f"Your cards are: {playerCard}")
    print(f"Your current score is: {playerScore}")
    print(f"Computer's hand contains: {computerCard[random.randint(1,100)%len(computerCard)]}")

def get_cards():
    playerCard.append(cards[(random.randint(1,100)%n)])

def logic():
    playerScore=0
    computerScore=0
    for num in playerCard:
        playerScore+=num
    for cp in computerCard:
            computerScore+=cp
    if playerScore>21:
        print(f"Your hand: {playerCard}\nYour score: {playerScore}")
        print(f"Computer hand: {computerCard}\nComputer score: {computerScore}")
        print("You lose 🥲")
    else:
        if playerScore==computerScore:
            print(f"Your hand: {playerCard}\nComputer hand: {computerCard}")
            print("It's a Draw")
        elif computerScore>playerScore and computerScore<21:
            print(f"Your hand: {playerCard}\nYour score: {playerScore}")
            print(f"Computer hand: {computerCard}\nComputer score: {computerScore}")
            print("You lose 🥲")
        else:
            print(f"Your hand: {playerCard}\nYour score: {playerScore}")
            print(f"Computer hand: {computerCard}\nComputer score: {computerScore}")
            print("You Win 🥳")
    

want_to_play()
while play:
    print(logo)
    distribute_card()
    show_card()
    choice=input("Want to get another card, 'y' for Yes and 'n' for No: ").lower()
    if choice=='y':
        get_cards()
    logic()
    want_to_play()
    os.system('cls')
print(logo)
print("Thank you for playing!!")


