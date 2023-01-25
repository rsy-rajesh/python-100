s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
print(s1.union(s2))
#s1.update(s2)     #ammend s1 with union of s1 and s2
print(s1, s2)
# s3 = s1.intersection(s2)
# s1.intersection_update(s2)
print(s1)
s4 = s1.difference(s2)
s5 = s1.symmetric_difference(s2)
print(s4)
print(s5)
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
s1.remove(2)    #through an error if element not found in set 
s1.discard(2)    # does not through error
item = s1.pop()
print(item)

#delete entire set 
#del s1
#print(s1)    # s1 was deleted trhough an error
s1.clear()  # clear or delete all elements of set
print(s1)




