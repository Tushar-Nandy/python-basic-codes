from wordlist import word_list
import random
target=random.choice(word_list)
n=len(target)
word=[]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def chckGuess(guess):
    for i in range(len(target)):
        if guess==target[i]:
            word[i]=guess  
        else:
            pass
    print(''.join(word))
    

def init():
    for _ in range(n):
        word.append('_')
    print(''.join(word),end=' ')

def takeGuess():
    guess=input("\nEnter a letter: ").lower()
    chckGuess(guess)

def main():
    count=6
    print("Welcome to the Hangman")
    init()
    print(stages[count])
    checkWord=''
    prevWord=''
    while(checkWord!=target and count!=0):
        takeGuess()
        checkWord=''
        for j in range(n):
            checkWord+=word[j]
        if(prevWord!=checkWord):
            prevWord=checkWord
        else:
            count-=1
            print(stages[count])
    if(checkWord==target):
        print("You win")
    else:
        print(f"You Lose\nThe word was {target}")

main()