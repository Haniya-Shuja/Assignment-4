def main():  # The main function that holds the logic of the program

    MIN_HEIGHT = 50  # Minimum height required to ride, set to 50

    while True:  # Infinite loop, which will continue until user provides no input (presses Enter without typing a height)

        height = input('How tall are you? (Press enter to stop):')  # Ask the user to input their height

        if not height:  # If the user presses Enter without typing anything, this condition will be True
            print("Good bye")  # Print "Good bye"
            break  # Break out of the loop and end the program

        height = int(height)  # Convert the input (which is a string) to an integer

        if height >= MIN_HEIGHT:  # If the user's height is greater than or equal to the minimum height
            print('You are tall enough to ride')  # Tell them they can ride

        else:  # If the user's height is less than the minimum height
            print("You are not tall enough to ride but maybe next year")  # Tell them they can't ride, but maybe next time

# The following line ensures that the main function will only run if this script is executed directly (not imported as a module)
if __name__ == '__main__':
    main()  # Calls the main function to run the program
