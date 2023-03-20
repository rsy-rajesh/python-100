# f =open('myfile.txt', 'r')
# while True:
#     line = f.readline()           # used to read file line by line
#     if not line:
#         break
#     print(line)

with open('myfile2.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
