st="gurugram"
print(st)
#Length of string
length=len(st)
print(length)
#String slicing
print(st[2:5]) # include 2 and exclude 5
print(st[0:])  #print all character after index 0, python assumes lenght of index in after :
print(st[0:-3])   #print 0 index to -3 counting from last character
print(st[0:len(st)-3]) # python automatically assumes -3 as len(st)-3
print(st[-1:6])  # len(st)-1 to 5  means 7 to 5 that is not valid  and it may be throws an error or print nothing
print(st[-4:8])  # len(st)-1 to 5  means 7 to 5 that is not valid  and it may be throws an error

x="harry"
print(x[-4:-2])  # explanation: len(x)-4 to -2 means 5-4=1, 1 to 5-2=3 i.e 1 to 3 inwich 3 will not include

