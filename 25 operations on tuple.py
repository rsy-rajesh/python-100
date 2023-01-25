# Tuples are immutable, hence if you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list. Then perform operation on that list 
# and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)  #count number of occurence of 3 in tuple1 
print('Count of 3 in Tuple1 is:', res)
print("\n\n\n")

# index() method
# The Index() method returns the first occurrence of the given element from the tuple.

Tuple1 = (0, 1, 2, 3, 2, 3, 3, 1, 3, 2)
res = Tuple1.index(3)  #return the index of first occurence of 3
print('Count of 3 in Tuple1 is:', res)
res1=Tuple1.index(3, 4, 8) # return index of occurence in between 4 and 8th index
print(res1)
res2=len(Tuple1)
print(res2)


