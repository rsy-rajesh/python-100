# A function is a block of code that performs a specific task whenever it is called. In bigger programs 
# where we have large amount of code, it is advisable to create or use existing functions that make the program flow organized and neat
# There are two types of function
# 1. Built-in-function: min(), sum(), range(), dict(), list() etc
# 2. User-Defined function: 

# create a function using the def keyword, followed by a function name , followed by a paranthesis() and a colon :


def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First Number is grater")
    else:
        print("Second Number is greater")

def Multiplication(a,b):
    pass #pass is used to write body later

#gmean
a=5
b=6
# gmean1=(a*b)/(a+b)
# print(gmean1)
calculateGmean(a,b)
isGreater(a,b)

c=7
d=9
# gmean2=(c*d)/(c+d)
# print(gmean2)
calculateGmean(c,d)
isGreater(c,d)
