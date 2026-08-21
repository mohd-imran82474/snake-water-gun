'''
1 for snake

-1 for water 

0 for gun 
'''
import random 
computer = random.choice([1,0,-1])
youstr = input("Enter your choice : ")
Dict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 : "snake" , -1 :"water" , 0 : "gun"}
you = Dict[youstr]

print(f"you choice {reverseDict[you]}\n computer choice {reverseDict[computer]}")
if (computer == you):
    print("The game is draw because imran boss played so goood")
else:
    if((computer - you) == -1 or (computer - you) == 2 ) :
        print("you loss")
    else:
        print("you win")
'''
else:
    if(computer == -1 and you == 1):
        print("you win")

    elif(computer == -1 and you == 0):
        print("you loss")

    elif(computer == 1 and you == -1):
        print("you loss")

    elif(computer == 1 and you == 0):
        print("you win ")

    elif(computer == 0 and you == -1):
        print("you win")

    elif(computer == 0 and you == 1):
        print("you loss")

    else:
        print("something went wrong")
'''


