# String formatting can be done in python using the format method.
# f-strings in python
# It is a new string formatting mechanism introduced by the PEP 498. It is 
# also known as Literal String Interpolation or more commonly as F-strings
#  (f character preceding the string literal). The primary focus of this mechanism is 
# to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the 
# f-string itself. The f-string can be formatted in much same as the str.format() method.
#  The f-string offers a convenient way to embed Python expression inside string literals for
#   formatting.

#Traditional method

letter= "Hi my name is {} and i am from {}"
country="India"
name="Rajesh"
print(letter.format(name, country))

letter= "Hi my name is {1} and i am from {0}"   # here priority of 0 will be high please run the program for more undestanding
country="India"
name="Rajesh"
print(letter.format(country, name))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.789678))

#F-STRING FINCTION

letter= "Hi my name is {} and i am from {}"
country="India"
name="Rajesh"
print(f"Hi my name is {name} and i am from {country}")
print(f"Hi my name is {{name}} and i am from {{country}}")   #print f string as it is

price=56.455664
txtt= f"for only { price:2f} dollers"
print(txtt)

print(f"{4*6}")
print(type(f"{5*4}"))


