#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

#Prompt the user to enter the first number.

#Read the input and convert it to an integer.

#Prompt the user to enter the second number.

#Read the input and convert it to an integer.

#Calculate the sum of the two numbers.

#Print the total sum with an appropriate message.

#The provided solution demonstrates a working implementation of this problem, where the main() 
# 
# function guides the user through the process of entering two numbers and displays their sum.

def main():
    print('This program adds two numbers.')
    
    # Get the first number from the user
    num1 = int(input('Enter the first number: '))  # Convert the input to an integer
    
    # Get the second number from the user
    num2 = int(input('Enter the second number: '))  # Convert the input to an integer
    
    # Calculate the sum
    total = num1 + num2
    
    # Print the result with a message
    print('The total is ' + str(total) + '.')

# Ensure the program runs only when executed directly
if __name__ == '__main__':
    main()
