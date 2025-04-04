import random

# Choices for the game
choices = ['rock', 'paper', 'scissors']

# User input
user_choice = input('Enter your choice (rock, paper, scissors): ').lower()

# Computer choice
computer_choice = random.choice(choices)

# Conditions for the game
if user_choice == computer_choice:
    print(f'Both have the same choice: Game tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(f'Player wins! {user_choice} beats {computer_choice}')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(f'Player wins! {user_choice} beats {computer_choice}')
elif user_choice == 'paper' and computer_choice == 'rock':
    print(f'Player wins! {user_choice} beats {computer_choice}')
else:
    print(f'Computer wins! {computer_choice} beats {user_choice}')
