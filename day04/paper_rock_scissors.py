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

#Write your code below this line 👇
options = [0, 1, 2]
user_option = int(
    input(
        'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
computer_option = random.choice(options)

if user_option >= 3 or user_option <0:
    print('You typed an invalid number, you lose!')
elif user_option == 0 and computer_option == 1:
    print(user_option)
    print(rock)
    print('Computer chose:')
    print(paper)
    print('You won!')
elif user_option == 0 and computer_option == 2:
    print(user_option)
    print(rock)
    print('Computer chose:')
    print(scissors)
    print('You won!')
elif user_option == 1 and computer_option == 0:
    print(user_option)
    print(paper)
    print('Computer chose:')
    print(rock)
    print('You lose!')
elif user_option == 2 and computer_option == 0:
    print(user_option)
    print(scissors)
    print('Computer chose:')
    print(rock)
    print('You lose!')
elif user_option == computer_option:
    print('It`s a tie')
elif user_option >= 3 or user_option <0:
    print('You typed an invalid number, you lose!')