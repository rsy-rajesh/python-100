

# st="Rajesh"
# coding = True
# if(coding):
#     if(len(st)>=3):
#         st= st[1:]+ st[0]
#         print(st)

# else:
#     pass


# st="Rajesh"
# coding = True
# if(coding):
#     if(len(st)>=3):
#         r1="abc"
#         r2= "jkh"
#         st= r1 + st[1:]+ st[0] + r2
#         print(st)

# else:
#     pass


st = input("Enter Message")
words = st.split(" ")
coding= input("1 for coding and 0 for decoding")
coding= True if (coding=="1") else False
if (coding):
    nwords = []
    for word in words:
        if (len(st) >= 3):
            r1 = "abc"
            r2 = "jkh"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
