import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_list = [rock, paper, scissors] # 0 = rock, 1 = paper, 2 = scissors

user_selection = int(input(
    "Welcome to the Rock Paper Scissors game!\n"
    "Choose a hand: \n"
    "Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_selection not in [0, 1, 2]:
    print("Invalid choice. Please, only choose 0, 1, or 2.")
    exit()

computer_selection = random.randint(0,2) # computer choice is also 0,1, or 2

print("You chose:")
print(rps_list[user_selection])

print("Computer chose:")
print(rps_list[computer_selection])

beats = {
    0:2, # Rock beats Scissors
    2:1, # Scissors beats Paper
    1:0 # Paper beats Rock
}

if user_selection == computer_selection:
    print("It's a tie!")

elif beats[user_selection] == computer_selection:
    print("You win!")
else:
    print("Computer wins!")
  
