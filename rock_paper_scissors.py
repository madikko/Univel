import random

trials = 3
score = 0
count = 0
options = ["rock","paper","scissors"]

while trials > 0:    
    computerChoice = random.choice(options)
    count += 1
    print("------------------------------------------------")
    print(f"Round {count}")
    print("------------------------------------------------")
    playerChoice = input("Hello player, select rock, paper or scissors:\n> ").lower()
    
    if playerChoice in options:
        if  ((playerChoice == "rock" and computerChoice == "scissors") or 
            (playerChoice == "paper" and computerChoice == "rock") or 
            (playerChoice == "scissors" and computerChoice == "paper")):
            trials -= 1
            score += 1
            print(f"You win this round your current score is {score}")
            print(f"Computer selected {computerChoice} and you selected {playerChoice}")
        elif playerChoice == computerChoice:
            trials -= 1
            score += 1
            print(f"It's a draw!")
            print(f"Computer selected {computerChoice} and you selected {playerChoice}")
        else:
            trials -= 1
            print(f"Computer wins this round.")
            print(f"Computer selected {computerChoice} and you selected {playerChoice}")            
    else:
        trials -=1
        print(f"Invalid input, you have {trials} trials left")
    
    print(f"You have {trials} trial(s) left")

print("Game Over!")
print(f"Your total score is {score}")