# There are 5 participants in the game
# all participants enter in the game by paying 5 rupees each 
# organizer set a magic number to win the game
# each contester enter a number to mach the magic number 
# if they match the number they win the whole winning price and all contester loose the game

print("********Welcome to Jungli Tank********")
print("""Game Instructions:
1. Maximum 5 contester can participate in the Game
2.Each contester pay the entry fee to participate in game
3. Entry fee is Rs.500
4. Only one participants can win the Game, if conflict price money divided into the contester
5. No refind will be given to you after entering the contest
6.There is punishment for cheating.  Thank You!!!!!""")

p1=input("Enter the 1st participants Name: ")
s1=int(input("Enter your secret number 1-5"))
p2=input("Enter the 2nd participants Name: ")
s2=int(input("Enter your secret number 1-5"))
p3=input("Enter the 3rd participants Name: ")
s3=int(input("Enter your secret number 1-5"))
p4=input("Enter the 4th participants Name: ")
s4=int(input("Enter your secret number 1-5"))
p5=input("Enter the 5th participants Name: ")
s5=int(input("Enter your secret number 1-5"))

sec=3
if(s1==sec):
    print("Congratulations ", p1, "You win the Game, Price Money will credit to you within few seconds")
elif(s2==sec):
    print("Congratulations ", p2, "You win the Game, Price Money will credit to you within few seconds")
elif(s3==sec):
    print("Congratulations ", p3, "You win the Game, Price Money will credit to you within few seconds")
elif(s4==sec):   
    print("Congratulations ", p4, "You win the Game, Price Money will credit to you within few seconds")
elif(s5==sec):
    print("Congratulations ", p5, "You win the Game, Price Money will credit to you within few seconds")