dic = {
    "Rajesh": "A goog guy",
    "India": "A Great Country"

}

print(dic["Rajesh"])

emp= {
    100: "Rajesh",
    101: "Neha",
    102: "Ram"

}

# print(emp["Rajesh"])  # key error
print(emp[100])

print(emp)
print(emp[102])     # if key not found in dictionary trhrough an error
print(emp.get(104))      # if key not found in dictionary return NONe

#Acess multiple keys in dictionary
print(emp.keys())
print(emp.values())


for key in emp.keys():
    print(emp[key])

for key in emp.keys():
    print(f"The value corresponding to the key {key} is {emp[key]}")

print(emp.items())

for key, value in emp.items():
    print(f"The key value corresponding to {key} is {value}")