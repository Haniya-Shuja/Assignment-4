import random
import string

def generate_strong_password(length=16):
    # Define characters that can be used in the password
    if length < 12:
        print("It's recommended to have a password length of at least 12 characters for better security.")
    
    all_characters = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and punctuation

    # Ensure the password contains at least one character from each category (uppercase, lowercase, number, symbol)
    while True:
        password = [
            random.choice(string.ascii_lowercase),  # At least one lowercase letter
            random.choice(string.ascii_uppercase),  # At least one uppercase letter
            random.choice(string.digits),           # At least one digit
            random.choice(string.punctuation)       # At least one special character
        ]
        
        # Fill the rest of the password length with random characters from the pool
        password += random.choices(all_characters, k=length - 4)
        
        # Shuffle the password to ensure randomness
        random.shuffle(password)
        
        # Join the list into a single string
        password = ''.join(password)
        
        # Check if the password meets the strength criteria
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the length of the password (recommended: 12 or more): "))
    strong_password = generate_strong_password(password_length)
    print(f"Generated strong password: {strong_password}")
