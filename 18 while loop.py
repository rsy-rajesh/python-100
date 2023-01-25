# for i in range(5):
#     print(i)

# i=0
# while(i<5):
#     print(i)
#     i=i+1
# print("out of while loop")

count = 5
while (count > 0):
    print(count)
    count = count-1

# Do-While loop in python
# do..while is a loop in which a set of instructions will execute at least once
# (irrespective of the condition) and then the repetition of 
# loop's body will depend on the condition passed at the end of the while loop. 
# It is also known as an exit-controlled loop.

# How to emulate do while loop in python?
# To create a do while loop in Python, you need to modify the while loop a bit 
# in order to get similar behavior to a do while loop.

# The most common technique to emulate a do-while loop in Python is to use an infinite 
# while loop with a break statement wrapped in an if statement that checks a given condition 
# and breaks the iteration if that condition becomes true:

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
