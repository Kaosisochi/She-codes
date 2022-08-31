
#Presented rock, paper, scissors game
print("""Welcome to the rock, paper, scissors game
Available choices are rock, paper or scissors""")
plays = ("rock", "paper", "scissors")
import random
computer_choice = random.choice(plays)
user_choice = input(str('Enter your choice: '))
print('Computer picked {} while You picked {}'.format(computer_choice, user_choice))

if user_choice == computer_choice:
    print("Both chose {} so it's a tie".format(user_choice))
elif user_choice == "rock" and computer_choice == "scissors":
    print("rock beats scissors so You win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("scissors cuts paper so You win")
elif user_choice == "paper" and computer_choice == "rock":
    print("paper covers rock so You win")
elif computer_choice == "rock" and user_choice == "scissors":
    print("rock beats scissors so Computer wins")
elif computer_choice == "scissors" and user_choice == "paper":
    print("scissors cuts paper so Computer wins")
elif (computer_choice == "paper") and (user_choice == "rock"):
    print("paper covers rock so Computer wins")
else:
    print("User's choice was invalid")

