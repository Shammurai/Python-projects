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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: \n"))
rps = [rock, paper, scissors]
print(rps[user_choice])
#random.randint allows you to assign a number to a list that can be called on at random
computer_choice = random.randint(0,2)
print("computer choose:")
print(rps[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you automatically lose.")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 2 and user_choice == 0:
    print("you lose!")
elif user_choice > computer_choice:
    print("you lose!")
elif computer_choice > user_choice:
    print("you win!")
elif  computer_choice == user_choice:
    print("Its a draw!")
