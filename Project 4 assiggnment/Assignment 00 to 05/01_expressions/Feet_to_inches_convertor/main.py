def main():
    # Prompt the user to enter a measurement in feet
    feet = float(input('Enter measurement in feet: '))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12

    # Print the result
    print(f'{feet} feet is equal to {inches} inches')

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
