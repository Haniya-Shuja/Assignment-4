def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit using the modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Prompt the user to enter a number
    print_ones_digit(num)  # Call the function with the user's input

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()