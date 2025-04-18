import random

DONE_LIKELIHOOD = 0.2  # Adjust this value to change how often we stop early

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # Stops execution if done() returns True
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == '__main__':
    main()