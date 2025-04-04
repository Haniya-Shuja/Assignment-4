# Mass-Energy Equivalence Calculator

# Speed of light constant in meters per second
SPEED_OF_LIGHT = 3.00 * 10**8

def main():
    print("Mass-Energy Equivalence Calculator")
    print("--------------------------------------------")
    
    while True:
        try:
            # Read the mass in kilograms from the user
            mass = float(input("Enter mass in kilograms (or type 'exit' to quit): "))
            
            # Calculate the equivalent energy using Einstein's equation E = mc^2
            energy = mass * SPEED_OF_LIGHT**2
            
            # Display the result
            print(f"The equivalent energy is: {energy} joules\n")
        
        except ValueError:
            # Exit if user types 'exit' or a non-numeric value
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
