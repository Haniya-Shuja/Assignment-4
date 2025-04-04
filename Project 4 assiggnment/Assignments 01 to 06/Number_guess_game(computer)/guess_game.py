import random

def guess_the_number():
    """Project:2  Guess the number by Computer"""
    number = random.randint(1, 100)
    guesses_left = 10
    print('Welcome to the number guessing game!')
    print("I am thinking of a number between 1 and 100.")
    
    while guesses_left > 0:
        print(f'\nYou have {guesses_left} guesses left.')
        
        try:
            guess = int(input('Take a guess: '))
        except ValueError:
            print('Invalid input: Please enter a valid number.')
            continue
        
        if guess > number:
            print('Too high! Try again.')
        elif guess < number:
            print('Too low! Try again.')
        else:
            print(f'Congratulations! You guessed the correct number in {11 - guesses_left} tries!')
            return
        
        guesses_left -= 1
    
    print(f'You ran out of guesses! The correct number was {number}.')

# Start the game
guess_the_number()
