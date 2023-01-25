# Lists are ordered collection of  data Items
# They stored multiple items in a single variable
# Lists are separated by commas and enclosed with square bracket []
# Lists are changable meaning we can alter them after cration

marks=[4,5,6,7,8]
# marks=[4,5,6,7,8,"Rajesh", true]  # python allow this 
print(marks)
print(marks[2])
print(type(marks))

print("\n\n\n")
print(marks[-3])  # Negative Indexing
print(marks[len(marks)-3])  # Positive Indexing
print(marks[5-3])
print(marks[2])

# Is element available in list
if 10 in marks:
    print("Yes Available")
else:
    print("The Given Number is Not Available")


if "Raj" in "Rajesh":
    print("Yes Match found")
else:
    print("No Match found")


# Print all marks
print(marks)
print(marks[:])  # pirnt(marks[0:len(marks)])
print(marks[1:])  #print(marks[1:len(marks)])
print(marks[2:4])
print(marks[1:5:2]) #marks[first-value:Last-value:Jump-Index] this program jump by 2 

# List comprehension 
# list comprehension are used for creating new list from other 
# interbals like list tuble dictionery sets and even in arrys and string
lst= [i for i in range(4)]
print(lst)

lst= [i*i for i in range(4)]
print(lst)

lst= [i for i in range(20) if i%2==0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)





