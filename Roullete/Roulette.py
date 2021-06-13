import random, time
name=input("Hello , please enter your name ")
gender=input("Please select H for He, S for She ")
x="Sir"
if gender=='H':
    x="Sir"
else:
    x="Ma'am"

if x=="Sir":
    print("Hello Mr.",name," Welcome to Roullete. I hope you went through the rules")
else:
    print("Hello Ms/Mrs.",name," Welcome to Roullete. I hope you went through the rules")

roullete_table=[[i for i in range(1,35,3)],[i for i in range(2,36,3)],[i for i in range(3,37,3)]]
print("Roullete Table")
print("0\t\t00")
for i in range(0,12):
    if i==1 or i==5 or i==9:
        w=""
        if i==1:
            w="First"
        elif i==5:
            w="Second"
        else:
            w="Third"
        print(roullete_table[0][i],"\t",roullete_table[1][i],"\t",roullete_table[2][i],"\t",w)
    elif i==2 or i==6 or i==10:
        print(roullete_table[0][i],"\t",roullete_table[1][i],"\t",roullete_table[2][i],"\t","Dozen")
    else:
        print(roullete_table[0][i],"\t",roullete_table[1][i],"\t",roullete_table[2][i])
cash=int(input("How much Chips do you want? "))

roullete_wheel=['00','0']
for i in range(1,37):
    roullete_wheel.append(str(i))


money=0
Bet=[]
Bet_on_no=[]
z="Yes"
while z=="Yes":
    print("----------------------------------------------------------------------------------------------------------------------")
    Bet=[]
    Bet_on_no=[]
    bet1=input("Enter 'E' if you want to place your bet on Even, Enter 'O' if you want to place your bet on Odd. And if you don't want to bet its alright. ")
    if bet1 in ['E','O']:
        x=int(input("Enter the amount of you want to bet on it "))
        Bet.append(x)
    else:
        Bet.append(0)
    bet3=input("Enter '1' if you want to bet on first Dozen (1-12). Enter '2' if you want to bet on second Dozen (13-24). Enter 3 if you want to bet on third Dozen (25-36). And if you don't want to bet its alright. ")
    if bet3 in ['1','2','3']:
        x=int(input("Enter the amount of you want to bet on it "))
        Bet.append(x)
    else:
        Bet.append(0)
    bet4=input("Enter '1' if you want to bet on first Column (1->34). Enter '2' if you want to bet on second Column (2-35). Enter 3 if you want to bet on third Column (3-36). And if you don't want to bet its alright. ")
    if bet4 in ['1','2','3']:
        x=int(input("Enter the amount of you want to bet on it "))
        Bet.append(x)
    else:
        Bet.append(0)
    bet5=[str(i) for i in input("Enter the Number from 00, 0, 1....36 to place bet on numbers. And if you don't place bets its alright. ").split()]
    Bet_on_no=[int(i) for i in input("Enter the amount you bet on each of the Numbers. ").split()]

    if sum(Bet)>=10 and sum(Bet_on_no)>=10 and sum(Bet)+sum(Bet_on_no)<=cash:
        amount=sum(Bet)+sum(Bet_on_no)
        cash=cash-(sum(Bet)+sum(Bet_on_no))
        print("Amount you Bet on ",amount," Cash in Hand Now ",cash)
        for qq in [1,2,3]:
            time.sleep(3)
            print(qq,end=' ')
        roll=random.choice(roullete_wheel)
        print("\nThe Ball is On ",roll)
        money=0
        if roll in bet5:
            money=money+(35*Bet_on_no[bet5.index(roll)])
        if int(roll)%2==0 and bet1=='E':
            money=money+(2*Bet[0])
        if int(roll)%2!=0 and bet1=='O':
            money=money+(2*Bet[0])
        if roll in roullete_table[0] and bet4=='1':
            money=money+(2*Bet[2])
        if roll in roullete_table[1] and bet4=='2':
            money=money+(2*Bet[2])
        if roll in roullete_table[2] and bet4=='3':
            money=money+(2*Bet[2])
        if int(roll)>=1 and int(roll)<=12 and bet3=='1':
            money=money+(2*Bet[1])
        if int(roll)>=13 and int(roll)<=24 and bet3=='2':
            money=money+(2*Bet[1])
        if int(roll)>=25 and int(roll)<=36 and bet3=='3':
            money=money+(2*Bet[1])

        cash=cash+money
        print("Amount you won ",money,"    Cash in Hand ",cash)
        if cash==0:
            z="No"
            print("You Lost All your Money....  :(")
            break
        z1=input("Press 'Y' to keep playing and 'N' to stop ")
        if z1=='Y':
            z="Yes"
        else:
            z="No"
        
    else:
        if x=="Sir":
            print("I am Sorry Mr.",name," but you can't play this round due to insufficient bets. Make sure the Inner bets are a total of atleast 10$ and so is the Outer bets.")
        else:
            print("I am Sorry Ms/Mrs.",name," but you can't play this round due to insufficient bets. Make sure the Inner bets are a total of atleast 10$ and so is the Outer bets.")
