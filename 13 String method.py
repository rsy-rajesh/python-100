x="Rajesh"
print(x)
print(len(x))
print(x.upper())
print(x.lower())
x="rajehs!!!!!!!!!!"
print(x.strip("!")) #returns the copy of leading and trailing whitespace removed
x="!!!!!!rajesh! !!!!!!!!!!"
print(x.strip("!"))

print(x.replace("rajesh", ("Ram"))) #replce rajesh with ram in variable x

print(x.split(" ")) #split make your string into list for example for this string "ram 45 tou" three list will be crated if you split by spaces

#capitalize: used to capatilixe the first character of string and the rest other character in lower case
blogpost="Introduction to python, you can use django to create web"
print(blogpost.capitalize())

str1="Welcome to India !!"
print(len(str1))
print(str1.count("India"))  #prodice occurence of India in str1=1
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

print(str1.endswith("!!"))
print(str1.endswith("c", 3, 4))
str1="India is a growing country, we will secure our future by doing investment in share market"
print(str1.find("is"))  #It return Index value of first occurence 
print(str1.find("hhghg")) #Reurn -1 if not found in your string
#print(str1.index("hfhfhf"))  #both find and index do same thing but index() through an error if no occurence found
# if we want if search value not foud after program will exit with error value

# isalnum() returns true only when your string is A-Z, a-z,0-9
# it returns false if any other character found

str1="Hirajesh780"
print(str1.isalnum())
str1="Hirajesh7 80"
print(str1.isalnum()) #Return false because of space

print(str1.isalpha()) #only return true if string made of a-z and A-Z
print(str1.islower()) #returns true if all character is in lower alphabets
print(str1.isprintable()) #return printable character
str2="HiRajesh\n"
print(str2.isprintable()) #returns false because \n is not printable charater

str1="India is grate"
print(str1.isspace())  #return true if your string contain spaces
print(str1.istitle()) #return true if  your title follows english title grammer formate
print(str1.startswith("India"))
print(str1.title())  #capitalize all starting word 
 




