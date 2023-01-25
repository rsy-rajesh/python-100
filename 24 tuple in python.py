tup= (4,5,6,7,8,9, True, "red")
print(type(tup), tup)

tup1= (1) # it is a int type not tuple if you want to create tuple with single element use comma
tup2=(1,)
print(type(tup1)) 
print(type(tup2)) 

# tup[2]=10  #through an error because tuple object does not support item assignment
print(tup[0])
# print(tup[1])
# print(tup[2])
print(tup[3])
print(tup[-3])
print(tup[:3])
print(tup[3:])
if 7 in tup:
    print("Number is present in tup")
else:
    print("Not present")

tup3=tup[2:6]
print(tup3)

