# Inheritance in python
# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

# Python Inheritance Syntax
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class
# Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

# Types of inheritance:
# Single inheritance
# Multiple inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance








# class employee:
#     def __init__(self, id , name):
#         self.id = id
#         self.name = name
#     def showdata(self):
#         print(f"employee name is {self.name} and IDis {self.id}")

# e1 = employee(1, "Rajesh")
# e1.showdata()








#inheritance

class employee:
    def __init__(self, id , name):
        self.id = id
        self.name = name
    def showdata(self):
        print(f"employee name is {self.name} and IDis {self.id}")


class programmer(employee):      #inheritance
    def showlanguage(self):
        print(f"The default language is programmer")

e2 = programmer(2, "ram")
e2.showdata()
e2.showlanguage()










