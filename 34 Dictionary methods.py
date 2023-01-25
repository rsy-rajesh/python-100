emp1 = {
    100: 60, 101: 70, 102: 65 
}

emp2 = {
    200: 40, 201: 20, 203: 45 
}
print(emp1)
emp1.update(emp2)
# emp2.clear()
print(emp1)
# emp1.pop(101)
emp2.pop(200)  # remove 200 key value pair
emp2.popitem()  # Remove last value pair 
print(emp2)

del emp2  # delete entire dictionary
del emp1[100]   #delete 100 key value pair only

