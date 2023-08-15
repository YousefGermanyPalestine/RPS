import random
choices = ["rock", "paper", "scissors"]
print("Rock-Paper-Scissors!")
while input("Play? (yes/no): ").lower() == "yes":
    user_choice = input("Rock, Paper, or Scissors? ").lower()
    comp_choice = random.choice(choices)
    print(f"You chose {user_choice}, computer chose {comp_choice}.")
    if user_choice == comp_choice:
        print("Its a draw between you and the robot!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        print("YOU win and the robot lost  !!!")
    else:
        print("  you lost and the ROBOT wins !!")





