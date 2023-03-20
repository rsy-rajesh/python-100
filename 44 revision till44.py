# a=input("Enter your number")
# print(type(a))
# print(a)

# a=int(input("Enter your number"))
# print(type(a))
# print(a)

# for i in range(3):
#     print("rajesh")
#     ++i


# Take multiple number as input and find sum usin function 
def sum(*num):
    for i in num:
        sum=sum+i
    return(sum)

x=sum(1,2,3,4,5)
print(x)

