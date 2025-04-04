import random

print('Guess the number between 1 to 100')

number = random.randint(1, 100)

while True:
    guess = int(input('Enter your guess number: '))

    if guess < number:
        print('Too low! Try again.')
    elif guess > number:
        print('Too high! Try again.')
    else:
        print('Congratulations! You got the correct number!')
        break
