import time
import random
print("Hello, welcome to rock, paper, scissors")
time.sleep(2)

# variables

choices = ['rock', 'paper', 'scissors']
enemychoices = ['rock', 'paper', 'scissors']
score = 0
enemyscore = 0

# main game loop
for i in range(6):
    choice = input("Please choose: rock, paper or scissors: ")
    
    enemychoice = random.choice(enemychoices)
    if choice == 'rock' and enemychoice == 'scissors':
        score += 1
        print("You got 1 point")

    elif choice == 'rock' and enemychoice == 'rock':
        print("Tie")

    elif choice == 'rock' and enemychoice == 'paper':
        print("The enemy got 1 point")
        enemyscore += 1

    elif choice == 'paper' and enemychoice == 'rock':
        score += 1
        print("You got 1 point")

    elif choice == 'paper' and enemychoice == 'paper':
        print("Tie")

    elif choice == 'paper' and enemychoice == 'scissors':
        print("The enemy got 1 point")
        enemyscore += 1

    elif choice == 'scissors' and enemychoice == 'paper':
        score += 1
        print("You got 1 point")

    elif choice == 'scissors' and enemychoice == 'scissors':
        print("Tie")

    elif choice == 'scissors' and enemychoice == 'rock':
        print("The enemy got 1 point")
        enemyscore += 1

print("You got: ", score)
print("The enemy got: ", enemyscore)
if score > enemyscore:
    print("You won")

elif enemyscore > score:
    print("You Lost")

else:
    print("No one won")

delay = input("Press enter to continue")
