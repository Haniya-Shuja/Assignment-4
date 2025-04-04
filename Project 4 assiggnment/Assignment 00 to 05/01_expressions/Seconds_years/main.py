def main():
    # Constants for time conversion
    DAYS_IN_YEARS = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECOND_IN_MINUTE = 60

    # Calculate the total number of seconds in a year
    seconds_in_year = DAYS_IN_YEARS * HOURS_IN_DAY * MINUTES_IN_HOUR * SECOND_IN_MINUTE

    # Print the result
    print(f'There are {seconds_in_year} seconds in a year.')

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
