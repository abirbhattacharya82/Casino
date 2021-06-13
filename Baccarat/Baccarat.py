import time, random
import random, time
name=input("Hello , please enter your name ")
gender=input("Please select H for He, S for She ")
x="Sir"
if gender=='H':
    x="Sir"
else:
    x="Ma'am"

if x=="Sir":
    print("Hello Mr.",name," Welcome to Baccarat. I hope you went through the rules")
else:
    print("Hello Ms/Mrs.",name," Welcome to Baccarat. I hope you went through the rules")

Shoe=[]
Shoe=['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J']
for _ in range(0,4):
    for i in range(2,10):
        Shoe.append(i)

cash=int(input("Please Enter the amount of Chip you want to cash in: "))
while(cash!=0):
    bet=0
    while(True):
        bet=int(input("Enter the Amount of Bet: "))
        if bet>cash:
            print("Insufficient Balance")
        else:
            break
    
    bets_on=input("Enter P to bet on Player, Enter B to bet on banker and Enter T to  bet on Tie: ")
    
    cash=cash-bet
    print("Bets=> ",bet," Cash in Hand=> ",cash)
    a=[]
    b=[]
    print("Dealer pulling Cards out of shoe")
    print("Player\tBanker")
    a.append(random.choice(Shoe))
    Shoe.remove(a[0])
    b.append(random.choice(Shoe))
    Shoe.remove(b[0])
    print(a[0],"\t",b[0])
    time.sleep(2)
    a.append(random.choice(Shoe))
    Shoe.remove(a[1])
    b.append(random.choice(Shoe))
    Shoe.remove(b[1])
    print(a[1],"\t",b[1])
    
    x=0
    y=0
    for i in a:
        if i=='A':
            x=x+1
        elif i=='K' or i=='Q' or i=='J':
            x=x+0
        else:
            x=x+i
    for i in b:
        if i=='A':
            y=y+1
        elif i=='K' or i=='Q' or i=='J':
            y=y+0
        else:
            y=y+i
    
    x=x%10
    y=y%10
    
    z=""
    if x>y:
        z="P"
    elif y>x:
        z="B"
    else:
        z="T"
    print(bets_on," ",z)
    if bets_on==z:
        cash=cash+(2*bet)
    if(cash==0):
        print("Sorry You lost all your money :(")
        break
    print("Keep Playing? Y for Yes aand N for N")

    
