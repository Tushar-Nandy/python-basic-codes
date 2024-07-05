import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
sufficientResources=True
def report():
    for key,value in resources.items():
        print(f"{key}: {value}")

profit=0
text=""
for key in MENU.keys():
    text+=key
    text+="/"

text=text[0:len(text)-1]

def makeCoffee():
    cash=0
    choice=input(f"What would you like to order {text}: ").lower()
    if choice=='report':
        report()
    else:
        if choice=='cappuccino' or choice=='espresso' or choice=='latte':
            print("Enter coins into the machine")
            qaurter=int(input("Enter the qaurters: "))
            dime=int(input("Enter the dime: "))
            nickle=int(input("Enter the nickle: "))
            cent=int(input("Enter the cent: "))
            cash= qaurter*0.25+dime*0.1+nickle*0.05+cent*0.01
            resDict=MENU[choice]
            ingridients=resDict['ingredients']
            cost=resDict['cost']
            change=cash-cost
            if change<0:
                print("Insufficient cash. Money refunded.")
            else:
                for key in resources:
                    if resources[key]<ingridients[key]:
                        print(f"Insufficinet resources: {key}. Money refunded")
                        return
                print(f"Here's your {choice}. ${change} returned")
                for key in resources:                            
                    resources[key]-=ingridients[key]
                
                        
        else:
            print("Invalid entry!")

    

while True:
    makeCoffee()
    i=input("Want more coffee: ").lower()
    if i=='yes':
        os.system('cls')
        continue
    else:
        break
       