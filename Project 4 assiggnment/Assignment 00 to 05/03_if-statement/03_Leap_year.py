def main():
    year = int(input('Enter a year:'))  # Take user input and convert it to an integer

    # Check if the year is divisible by 4 but not 100, or divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('That\'s a leap year')  # Print if it's a leap year
    else:
        print('That\'s not a leap year')  # Print if it's not a leap year

# Call the main function to run the program
if __name__ == '__main__':
    main()


