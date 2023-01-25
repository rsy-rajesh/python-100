# Create a program like KBC
# set question and answer 
winamount=0
q=["Name of Indian PM", "Name of India's President", "Area of Circle", "list in python created by", "tuple in python created by", "Gita is written by"]
for i in q:
    print(i)
    if i=="Name of Indian PM":
        ans=int(input("Enter Answer: \n 1. Narendra Modi \n 2. Rajesh Yadav \n 3. Droupadi Murmu \n 4. Arvind Kejriwal\n"))
        if ans==1:
            winamount=winamount+500
            print("Congratulations, You have won 500")
            print("Your total  winning price :", winamount)
            print("\n\n ")
        else:
            print("Incorrect Answer, Your Game is over Now!!, But you still get your price amount: ", winamount)
            print("\n\n ")
            break
    elif i=="Name of India's President":
        ans=int(input("Enter Answer: \n 1. Narendra Modi \n 2. Rajesh Yadav \n 3. Droupadi Murmu \n 4. Arvind Kejriwal\n"))
        if ans==3:
            winamount=winamount+1000
            print("Congratulations, You have won 1000")
            print("Your total  winning price :", winamount)
            print("\n\n ")
        else:
             print("Incorrect Answer, Your Game is over Now!!, But you still get your price amount: ", winamount)
             print("\n\n ")
             break
    elif i=="Area of Circle":
        ans=int(input("Enter Answer : \n 1. (22/7)r*r \n 2. (22/7)r*r*r \n 3. (3.155)r*r \n 4. A(3.14)r*r*r \n"))
        if ans==1:
            winamount=winamount+5000
            print("Congratulations, You have won 5000")
            print("Your total  winning price :", winamount)
            print("\n\n ")
        else:
             print("Incorrect Answer, Your Game is over Now!!, But you still get your price amount: ", winamount)
             break
    elif i=="list in python created by":
        ans=int(input("Enter Answer: \n 1. using curely bracket{} \n 2. Using big bracket[] \n 3. Using small bracket() \n 4. Using Doller $\n"))
        if ans==2:
            winamount=winamount+10000
            print("Congratulations, You have won 10000")
            print("Your total  winning price :", winamount)
            print("\n\n ")
        else:
             print("Incorrect Answer, Your Game is over Now!!, But you still get your price amount: ", winamount)
             break

    elif i=="tuple in python created by":
        ans=int(input("Enter Answer: \n 1. using curely bracket{} \n 2. Using big bracket[] \n 3. Using small bracket() \n 4. Using Doller $\n"))
        if ans==3:
            winamount=winamount+80000
            print("Congratulations, You have won 80000")
            print("Your total  winning price :", winamount)
            print("\n\n ")
        else:
             print("Incorrect Answer, Your Game is over Now!!, But you still get your price amount: ", winamount)
             break

    elif i=="Gita is written by":
        ans=int(input("Enter Answer: \n 1. Maharshi Balmiki \n 2. Shree Krishna \n 3. Vidur \n 4. Maharshi Wed Vyas \n"))
        if ans==4:
            winamount=winamount+100000
            print("Congratulations, You have won 100000")
            print("Your total  winning price :", winamount)
            print("\n\n ")
            print("***********************congratualtions You have won the KBC season-2022****************************")
        else:
             print("Incorrect Answer, Your Game is over Now!!, But you still get your price amount: ", winamount)
             break
