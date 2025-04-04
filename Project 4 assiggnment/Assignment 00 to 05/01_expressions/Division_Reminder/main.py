def main():
    # Prompt the user for the dividend
    dividend = int(input('Please enter an integer to divide by: '))

    # Ask for a divisor, ensuring it's not zero (to avoid ZeroDivisionError)
    divisor = int(input('Please enter a divisor: '))

    # Check if the divisor is zero to prevent a ZeroDivisionError
    if divisor == 0:
        print("Error: Cannot divide by zero.")
    else:
        # Perform the division and calculate the remainder
        quotient = dividend // divisor  # Integer division
        remainder = dividend % divisor  # Modulo operation for remainder

        # Print the result
        print(f'The result of this division is {quotient} with a remainder of {remainder}')

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
