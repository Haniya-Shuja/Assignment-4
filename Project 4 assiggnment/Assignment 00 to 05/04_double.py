def double(num):
    return num * 2

def main():
    try:
        user_input = float(input("Enter a number: "))
        result = double(user_input)
        print(f"Double that is {result}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()