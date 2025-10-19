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
import random

# player_choice = int(input("Enter '1' for Rock, '2' for Paper, '3' for Scissors\n"))
# computer_choice = random.randint(1, 3)
# rock_choice = player_choice[1]
# paper_choice = player_choice[2]
# scissors_choice = player_choice[3]
# print(computer_choice)

# if player_choice == computer_choice == 1:
#     print("Your Choice")
#     print(rock)
#     print("Computer Choice")
#     print(rock)
#     print("It's a draw!")
#
# elif player_choice == computer_choice == 2:
#     print("Your Choice")
#     print(paper)
#     print("Computer Choice")
#     print(paper)
#     print("It's a draw!")
#
# elif player_choice == computer_choice == 3:
#     print("Your Choice")
#     print(scissors)
#     print("Computer Choice")
#     print(scissors)
#     print("It's a draw!")
#
# elif player_choice == 1 and computer_choice == 3:
#     print("Your Choice")
#     print(rock)
#     print("Computer Choice")
#     print(scissors)
#     print("It's a win!")
#
# elif player_choice == 2 and computer_choice == 1:
#     print("Your Choice")
#     print(paper)
#     print("Computer Choice")
#     print(rock)
#     print("It's a win!")
#
# elif player_choice == 3 and computer_choice == 2:
#     print("Your Choice")
#     print(scissors)
#     print("Computer Choice")
#     print(paper)
#     print("It's a win!")
#
# elif player_choice == 3 and computer_choice == 1:
#     print("Your Choice")
#     print(scissors)
#     print("Computer Choice")
#     print(rock)
#     print("It's a lose!")
#
# elif player_choice == 1 and computer_choice == 2:
#     print("Your Choice")
#     print(rock)
#     print("Computer Choice")
#     print(paper)
#     print("It's a lose!")
#
# elif player_choice == 2 and computer_choice == 3:
#     print("Your Choice")
#     print(paper)
#     print("Computer Choice")
#     print(scissors)
#     print("It's a lose!")
#
# else:
#     print("Invalid number. You lose!")

player_choice = int(input("Enter '0' for Rock, '1' for Paper, '2' for Scissors\n"))
computer_choice = random.randint(0, 2)
game_shapes = [rock, paper, scissors]
if player_choice <=2 and player_choice >=0:
    print(game_shapes[player_choice])
    print("computer choice:")
    print(game_shapes[computer_choice])

if player_choice >= 3:
    print("Invalid number. You lose!")
elif player_choice == computer_choice:
    print("It's a draw")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif player_choice < computer_choice:
    print("You lose!")

input("Press any key to end...")