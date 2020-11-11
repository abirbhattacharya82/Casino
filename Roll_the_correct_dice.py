import random
k=int(input("Enter your Total Balance in the Account: "))
bet=int(input("Place your Bets: "))
if bet>k:
    print("Unable to Place Bet")
else:
    j=int(input("Guess the Number on the Dice: "))
    x=random.randint(1,6)
    if x==j:
        print("You Won")
        bet=bet+bet
        k=k+bet
        print("Current Balance: ",k)
    else:
        print("You Lost")
        k=k-bet
        print("Current Balance: ",k)
