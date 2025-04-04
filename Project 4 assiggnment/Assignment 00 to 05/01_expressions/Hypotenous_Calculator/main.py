import math

def main():
    # Prompt the user to enter the lengths of the sides
    side_ab = float(input('Enter the length of AB: '))
    side_ac = float(input('Enter the length of AC: '))

    # Calculate the hypotenuse (BC) using the Pythagorean theorem
    hypotenuse_bc = math.sqrt(side_ab**2 + side_ac**2)

    # Print the result, rounding to two decimal places
    print(f'The length of BC (the hypotenuse) is: {hypotenuse_bc:.2f}')

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
