import random

words = ['biryani', 'kabab', 'tikka', 'fries', 'barBQ', 'kachori','faloda','tahari']

word = random.choice(words)
guessed_letters = []
attempts = 6

print('Welcome to Hangman game!')
print('_' * len(word))  # Display underscores for the word length

while attempts > 0:
    guess = input('\nGuess a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Please enter one letter only.')
        continue

    if guess in guessed_letters:
        print('This letter was already guessed. Please choose another one.')
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f'Wrong guess! Attempts remaining: {attempts}')

    # Display the current state of the word
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(displayed_word)

    if '_' not in displayed_word:
        print(f'Congratulations! The correct word is {word}. You win!')
        break
else:
    print(f'Game over! The correct word was: {word}')
