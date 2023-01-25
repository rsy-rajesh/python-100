def average(a,b):
    print("The Average  is ", (a+b)/2)

average(5,7)

# There are four types of arguments that we can provide in a function
# Default Arguments 
# Keyword Arguments
# Variable lengh Arguments
# Required Arguments

# 11111111111111.      Default Arguments 
# def average(a=2,b=4):   #Default value passing if no value provided
#     print("The Average  is ", (a+b)/2)

# average(8,7)  #passing value of a and b
# average(6,)  #passing value of a
# average(b=10)  # passing value of b
# # if we did not pass the value default as a=2 and b=4 will be assumed
# average() 

# def name(fname, mname="kumar", lname="Yadav"):
#     print(fname, mname, lname)

# name("rajesh")
# name("rajesh", "kr")

# #222222222222222222222. Keyword Arguments
# We can provide arguments with key=value, this way the interpreter recognizes the 
# arguments by the parameter name. Hence the the order in which  the arguments    are passed does not matter 

average(b=20, a=6)

#333333333333333333. Required Arguments
# In most top of program average function a and b are required arguments, if you did not pass python through error

#444444444444444444. Variable length Arguments 
def avg(*numbers):  # one star is used for interger and double star used for string / dictionertu
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ", sum/len(numbers))

avg(4,5,6,7)
avg(1,2)

def name(**name):
    print("Hello, ", name["fname"], name["lname"])

name(fname="rajesh", lname="kr")

# Return Statement

def avg(*numbers):  # one star is used for interger and double star used for string / dictionertu
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is: ", sum/len(numbers))
    return sum/len(numbers)

x=avg(1,2,3,4,5)
print(x)

# Return only runs one time if you use multiple return in function, only first return will be executed


