import random  # Import the random module to generate random numbers

def main():
    # Start a loop that runs 3 times (for 3 dice rolls)
    for roll in range(1, 4):  # range(1, 4) means the loop will run for 1, 2, and 3
        die1 = random.randint(1, 6)  # Simulate rolling the first die (random number between 1 and 6)
        die2 = random.randint(1, 6)  # Simulate rolling the second die (random number between 1 and 6)
        
        # Print the result of the current roll
        print(f'Roll {roll} Die1 = {die1}, Die2 = {die2}')  

# This part ensures the program runs only when the script is executed directly (not when imported as a module)
if __name__ == '__main__':  # The colon is required to indicate the start of the block
    main()  # Call the main function to start the dice rolling process
