import random
print("Here's your chance to win Huge prize")
print("All you have to do is guess what will be falling when we will be tossing the coin")
k=0
print("Your current balance=> ",k)
print("Choose H for Heads and T for Tails.")
c=input()
while(True):
    s=100
    x=random.randint(1,2)
    if x==1 and (c=='H' or c=='h'):
        print("You won ",s,"$")
        k=k+s
    elif  x==2 and (c=='T' or c=='t'):
        print("You won ",s,"$")
        k=k+s
    else:
        print("You Lost all your Monney..... :(")
        break

    print("Do you want to walk away with your money or  you want to keep playing Y/N")
    c2=input()
    if c2=='N' or c2=='n':
        print("Wise men and women often take a step back. Good Choice. Your current Balance=> ",k)
        break
    print("Your current balance=> ",k)
    print("Choose H for Heads and T for Tails.")
    c=input()
    s=s+100

