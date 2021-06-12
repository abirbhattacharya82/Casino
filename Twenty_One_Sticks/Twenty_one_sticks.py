print("WARNING: YOU WILL NEVER WIN THIS GAME")
x=21
while x>1:
    x_i=int(input("Pick up 1-4 sticks "))
    if x_i>4 or x_i<1:
        print("Illegal You are Disquallified")
		break
    else:
        x=x-5
        y=(5-x_i)
        print("I pick ",y," sticks")
        print("Sticks Remaining: ",x)
print("You Lost")
print(":(")
