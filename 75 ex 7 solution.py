import os 
# files = os.listdir("cluter")
# for file in files:
#     print(file)





# os.rename("cluter/test.txt", "cluter/test123.txt")





# files = os.listdir("cluter")
# for file in files:
#     if file.endswith(".png"):
#         print(file)




files = os.listdir("cluter")
i = 1
for file in files:
    
    if file.endswith(".png"):
        print(file)
        os.rename(f"cluter/{file}", f"cluter/{i}.png")
        i = i+1


 