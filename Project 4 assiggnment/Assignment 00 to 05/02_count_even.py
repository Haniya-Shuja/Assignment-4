def count_even():
    numbers = []
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            numbers.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    
    even_count = sum(1 for num in numbers if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

def main():
    count_even()

if __name__ == '__main__':
    main()