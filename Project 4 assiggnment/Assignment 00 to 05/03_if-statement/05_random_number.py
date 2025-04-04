import random

def main():  # Define the main function to organize your code

    for i in range(10):  # Loop 10 times to generate 10 random numbers
        number = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(number, end=' ')  # Print the number, separated by spaces

    print()  # Print a newline at the end for formatting

# Ensure that the script only runs the main function when it's executed directly
if __name__ == '__main__':
    main()
