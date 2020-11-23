import random
x=['A','B','C','D']
w=5000
print('You have 5000$')
p=int(input('Place your Bet '))
w=w-p
y=int(input('Pull The Lever by pressing 1 '))
if y==1:
    a1=random.randint(0,3)
    b1=random.randint(0,3)
    c1=random.randint(0,3)
    if a1==b1 and b1==c1:
        print('You Seem to be Lucky')
        p=p+p
        w=w+p
    else:
        print('Looks Like you are Having a Bad Day')
print('_________')
print(x[a1],'|',x[b1],'|',x[c1])
print('_________')
print('Your Current Balance=> ',w)

