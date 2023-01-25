# The match case consists of three main entities :

# The match keyword
# One or more case clauses
# Expression for each case
# The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

# Syntax:
# match variable_name:
#             case ‘pattern1’ : //statement1
#             case ‘pattern2’ : //statement2
#             …            
#             case ‘pattern n’ : //statement n
# Example:
# x = 4
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
#     # Empty case with if-condition
#     case _ if x < 10:
#         print("x is < 10")
#     # default case(will only be matched if the above cases were not matched)
#     # so it is basically just an else:
#     case _:
#         print(x)

x=int(input("Enter Your Number"))
match x:
    #if x is 0
    case 0 if x==0:
        print("x is Zero")
    #case with if condition and x=2
    case 2 if x%2==0:
        print("X%2 ==0 and case is 4")
    #default case
    case _ if x==10:
        print("x is 10") 
    case _ if x==30:
        print("x is 30") 
    case _: 
        print("Default case")
    