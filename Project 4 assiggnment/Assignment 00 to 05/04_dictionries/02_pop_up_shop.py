def main():
    # Define the prices for different fruits
    fruit_prices = {
        'apple': 3.5,
        'mango': 4.0,
        'kiwi': 2.5,
        'jackfruit': 10.0
    }
    
    total_cost = 0  # Initialize total cost to 0

    print('Welcome to the Fruit Shop')

    # Iterate through the fruit and price pairs in the dictionary
    for fruit, price in fruit_prices.items():
        # Prompt the user for the quantity of each fruit they want to buy
        quantity = input(f'How many {fruit}s do you want? ')  # Use f-string for string formatting
        
        # If the input is a valid number, calculate the total cost for that fruit
        try:
            quantity = int(quantity)  # Convert quantity to an integer
            total_cost += quantity * price  # Add the cost of this fruit to the total cost
        except ValueError:
            print(f'Invalid input for {fruit}. Please enter a valid number.')

    # Display the total cost after the loop
    print(f'Your total cost is ${total_cost:.2f}')

# Call the main function to run the program
if __name__ == '__main__':
    main()

