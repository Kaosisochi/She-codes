print("Rock, paper, scissors game")
plays = ["rock", "paper", "scissors"]
user = str(input('''Which do you choose;
rock, paper or scissors: '''))
import random
sys_choi = random.choice(plays)
print('System choice:', sys_choi)
if (user == sys_choi):
    print("It's a tie")
if (user == "rock" and
        sys_choi == "scissors"):
    print("You win")
if (user == "scissors" and
        sys_choi == "rock"):
    print("System wins")
if (user == "paper" and
        sys_choi == "rock"):
    print("You win")
if (user == "rock" and
        sys_choi == "paper"):
    print("System wins")
if (user == "scissors" and
        sys_choi == "paper"):
    print("You win")
if (user == "paper" and
        sys_choi == "scissors"):
    print("System wins")
