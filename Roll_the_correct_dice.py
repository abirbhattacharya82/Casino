import random
print("you have 5000 rupees in your account")
k=5000
f=5
while (True):
    bet=int(input("Place your Bets: "))
    if bet>k:
        print("Unable to Place Bet")
    else:
        j=int(input("Guess the Number on the Dice: "))
        x=random.randint(1,7)
        if x == j:
            print("You Won")
            bet=bet+bet
            k = k+bet
            print("Current Balance: ",k)
        else:
            print("You Lost")
            k=k-bet
            print("Current Balance: ",k)
            f=f-1
    if(k==0):
        break
    elif(f==0):
        break
