import os 
from logo import logo
bid_history={}
running=True
maxBid=-999999
maxBidder=""
while running:
    print(logo)
    name=input("Enter your name: ").capitalize()
    bid=int(input("Enter your bid (in Rs.): "))
    bid_history[name]=bid
    morePlayers=input("Are there more bidders? Yes(y) or No(n): ").lower()
    if morePlayers=='n':
        running=False
    else:
        os.system('cls')

for key in bid_history:
    if bid_history[key]>maxBid:
        maxBid=bid_history[key]
        maxBidder=key
print("\n")
print(f"The max bidder is {maxBidder} with a bid of Rs. {maxBid}")
    

