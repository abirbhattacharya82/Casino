import math
import time
s1=0
s2=0
r=[1,2,3,4,5,6]
f=1
while (s1<=21 or s2<=21):
    print("To Throw Dice Enter 1 ")
    x=input()
    if x!=1:
        print("You Chickened Out!")
        break
    if 
    d1=math.random(r)
    if f==1:
        d2=math.random(r)
    print("Dice 1=> ",d1,"Dice 2=> ",d2)
    s1=d1+d2
    print("Your Total=> ",s1)
        
    print("Computer's Turn ")
    d1=math.random(r)
    d2=math.random(r)
    print("Dice 1=> ",d1,"Dice 2=> ",d2)
    s2=d1+d2
    print("Computer's Total=> ",s2)
    