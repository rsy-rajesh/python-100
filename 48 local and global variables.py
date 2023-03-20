# x= 5
# print(x)

# def func():
#     x=10
#     y=2
#     print("value of local x: ", x)

# func()

    
# print(y)       # trough an error because y is not define in global

x= 5
print(x)

def func():
    global x
    x = 20        #here global variable x was changed
    y=2
    print("value of global variable  x: ", x)

func()

  