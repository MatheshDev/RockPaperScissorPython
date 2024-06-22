import random

def AIchoice():
    option = ["rock","paper","scissor"]
    AIchoice = random.choice(option)
    return AIchoice
AIscore = 0
Pscore = 0

while AIscore <= 9 and Pscore <= 9:
    print("Rock, Paper, Scissor")
    playerChoice = str(input("Please Enter a option : ")).lower()   
    AI = "paper"
    if(playerChoice not in ["rock","paper","scissor"]):
        print("Please Choose a correct option")
        continue
    if(playerChoice == AI):
        print("Tie")
    elif((playerChoice == "rock" and AI == "scissor") or (playerChoice == "paper" and AI == "rock") or (playerChoice == "scissor" and AI == "paper")):
        print("AI : ", AI, "Player : ",playerChoice)
        print("Player Wins a Point")
        Pscore = Pscore + 1
        print("Player : ",Pscore,"AI : ",AIscore)
    elif((AI == "rock" and playerChoice == "scissor") or (AI == "paper" and playerChoice == "rock") or (AI == "scissor" and playerChoice == "paper")):
        print("AI : ", AI, "Player : ",playerChoice)
        print("AI wins a point")
        AIscore = AIscore + 1
        print("AI : " ,AIscore,"Player : ",Pscore)

if(AIscore > Pscore):
    print("AI Wins!")
else:
    print("Player Wins")