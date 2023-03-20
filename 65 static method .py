
# Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.








class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b


# result=math.add(1,2)
# print(result)
a= math(5)
print(a.num)
a.addtonum(7)
print(a.num)
print(math.add(5,8))
print(a.add(7,5))

