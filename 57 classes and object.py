# Python Class and Objects
# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# Creating a Class:
# Let us now create a class using the class keyword.

# class Details:
#     name = "Rohan"
#     age = 20









# class emp:
#     name = "Name"
#     occupaiton = "occupation"
#     networth = "10"


# print(emp.name)
# print(emp.networth)

# a = emp()
# a.name = "Rajesh"
# a.occupaiton = "System Administrator"
# a.networth = "10000"


# print(a.name)










class emp:
    name = "Name"
    occupation = "occupation"
    networth = "10"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

emp1 = emp()
emp1.name= "Rajesh"
emp1.occupation= "Managing Director"
emp1.networth= "112345300000000"

emp1.info()

emp2= emp()
emp2.info()

emp3 = emp()
emp3.name= "Ram"
emp3.occupation= "God"
emp3.networth= "No Limit"
emp3.info()