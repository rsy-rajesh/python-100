def cube(x):
    return x*x*x

l = [2,3,4,5,6,7,8,9]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)
