# Indentation
a= int(input("Enter your Age: "))
if(a<=18 and a>0):
    if(a>=15):
        print("You can drive in free spaace")
    elif(a>=12 and a<15):
        print("you can think to drive")
    else:
        print("You are now kid, play with your father")
elif(a>18):
    print("You can drive, Drive safely")
else:
    print("Enter the valid age")

    
