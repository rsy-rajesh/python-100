# # problem statement 

# # two players 
# # have three choices 
# # 6 possibilities 
# # s w g      s w g 
# # s------s          0
# # s------w         snake Win 
# # s------g         gun win 
# # w------w        0
# # w------g          water win 
# # g------g          0


# score_player1=0
# score_player2=0

# print("*****This game required two player*****")
# max=int(input("How many time you want to play\n"))

# for i in range(max):
#     while(True):

#         print("Player 1. ")
#         player1= int(input("Enter numeric value \n1. Snake\n 2. Water \n 3. Gun\n"))

#         print("\n\nPlayer 2. ")
#         player2= int(input("Enter numeric value\n1. Snake\n 2. Water \n 3. Gun\n"))

#         if(player1==player2):
#             print("\nNo result\n")
#         elif(player1==1 and player2==2):
#             score_player1=score_player1 + 10
#             print("Player1 score is ", score_player1)
            
#         # elif(player2==2 and player1==1):
#         #     score_player1=score_player1 + 10
#         #     print("Player1 score is ", score_player1)
#         elif(player1==1 and player2==3):
#             score_player2=score_player2+10
#             print("player2 score is ", score_player2)

#         # elif(player2==3 and player1==1):
#         #     score_player2=score_player2+10
#         #     print("player2 score is ", score_player2)

#         elif(player2==2 and player1==3):
#             score_player2=score_player2+10
#             print("player2 score is ", score_player2)

#         # elif(player1==3 and player2==2):
#         #     score_player2=score_player2+10
#         #     print("player2 score is ", score_player2)

# if(score_player1==score_player2):
#     print("Game drow You both player have same SCORE:", score_player1)
# elif(score_player1>score_player2):
#     print("Player1 won the Game with", score_player1-score_player2, "Numbers")
# elif(score_player2>score_player1):
#     print("Player2 won the Game with", score_player2-score_player1, "Numbers")




import random

def check(comp, user):
    if(comp==user):
        return 0
    elif(comp==1 and user==2):
        return 1
    elif(comp==2 and user==3):
        return 1
    elif(comp==3 and user==1):
        return 1
    else:
        return 2
    

comp= random.randint(1, 3)
user= int(input("Enter 1.for Snake  2.for water 3.for Gun\n"))
print(f"Computer chooses {comp}")
print(f"You chooses {user}")

score = check(comp, user)
if(score==0):
    print("\n Match drow")
elif(score==1):
    print("\nComputer Win")
else:
    print("\n You win")



