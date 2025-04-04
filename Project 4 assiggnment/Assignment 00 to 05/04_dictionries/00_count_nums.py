def main():
    numbers = []  # List to store user inputs

    while True:
        user_input = input('Enter a number or press Enter to finish: ')  # Ask the user for input

        if user_input == "":  # If the user presses Enter without entering a number, break the loop
            break

        numbers.append(int(user_input))  # Convert the input to an integer and add it to the numbers list

    # Now count the occurrences of each number
    occurrences = {}  # Dictionary to store the count of each number

    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1  # If the number already exists in the dictionary, increment its count
        else:
            occurrences[number] = 1  # If the number is not yet in the dictionary, add it with count 1

    # Print the number and how many times it appears
    for number, count in occurrences.items():
        print(f'{number} appears {count} times.')

# Ensure the main function is called when the script is executed
if __name__ == '__main__':
    main()






