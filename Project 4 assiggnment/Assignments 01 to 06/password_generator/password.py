import random
import string

# Function to generate password
def password_generator(length=12):
    # Available characters: lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password of the given length by randomly choosing characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask the user for the desired password length
length = int(input('Enter your desired length for the password: '))

# Generate the password
password = password_generator(length)

# Print the generated password
print(f'Desired password: {password}')
