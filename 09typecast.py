a="1"
b="2"
c=5
print(a+b)
#this print function show you 12 because both a nad ba are integer
#without typecasting python take this input as string
a="1"
b="2"
print(int(a)+int(b))  #Explicit typecating
#print(a+c) # though an error

#Here result converted to integer before printing the result
#Typecasting: The conversion of one data type to another data type is known as typecasting
#Python support a wide variety of functions or method like: in(), float(), str(), ord(), oct(), tuple(), set(), list(), dict()
#there are two types of Typecasting
#1. Explicit conversion: user define maually "1"+"2"=3
#2.Implicit conversion: python can do automatically like 5+3.4=8.4


#Implicit typecating
x=6.2
y=5
print(x+y) #Here result will be float value 
print(y+x)
print(type(y))
print(type(x))
