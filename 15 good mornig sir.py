import time
t=time.strftime('%H:%M:%S')
print(t)
time1=int(time.strftime('%H'))
print(time1)

# time1=int(input("Enter time in Hour only 1-21\n :"))
if(time1>=0 and time1<=12):
    print("Good Morning Sir")
elif(time1>12 and time1<=16):
    print("Good Afternoon Sir")

elif(time1>16 and time1>=19):
    print("Good Evening Sir")
elif(time1>19 and time1<=23):
    print("Good Night")
else:
    print("Time Error")

# import time
# timestamp=time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp=int(time.strftime('%H'))
# print(timestamp)
# h=timestamp
# timestamp=int(time.strftime('%M'))
# print(timestamp)
# m=timestamp
# timestamp=int(time.strftime('%S'))
# print(timestamp)
# s=timestamp



