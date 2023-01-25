l= [5,6,7,8,9,3,4,5]
print(l)
# l.append(10)  # append the list with 10 at last index
# print(l)
# l.sort()
# print(l)  #sort the list in assending order
# l.sort(reverse=True) # sort the list in discending order
# print(l)
l.reverse()  # reverse the original list 
print(l)
print(l.index(4))  # return the index of 4 in list if not found in the list through an error
#index function only returns the first index
print(l.count(5))  # count the occurence of 5 in list l
m=l    # here m is a reference of l not all value copied to m
m[0]=0  # value of index o will be changed in list l
print(m)
print(l)
m=l.copy()  #copy the content of l into m
print(m)
print("\n\n\n")

x=[4,6,7,8,9,10]
print(x)
x.insert(1, 900)  #insert 900 at the index 1 in list x
print(x)

l.extend(x)  # copy all value of x at the end of list l
print(x)
print(l)

a=[6,66,6666,666]
b=[7,77,777,7777]
k=a+b   #concatenating two list
print(k)


