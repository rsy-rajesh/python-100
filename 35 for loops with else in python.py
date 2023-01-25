for i in range(5):
    print(i)

else:
    print("Sorry no i")
#Here else statement runs after completion of for loop

for i in range(5):
    print(i)
    if i==4:
        break

else:
    print("Sorry no i")

#Here else statement not run because for loop was break


