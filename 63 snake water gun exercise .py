
import random

def check(comp, user):
    if(comp==user):
        return 0
    elif(comp==1 and user==2):
        return 1
    elif(comp==2 and user==3):
        return 1
    elif(comp==3 and user==1):
        return 1
    else:
        return 2
    

comp= random.randint(1, 3)
user= int(input("Enter 1.for Snake  2.for water 3.for Gun\n"))
print(f"Computer chooses {comp}")
print(f"You chooses {user}")

score = check(comp, user)
if(score==0):
    print("\n Match drow")
elif(score==1):
    print("\nComputer Win")
else:
    print("\n You win")