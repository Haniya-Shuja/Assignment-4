import time

# Function for countdown timer
def countdown_timer(seconds):
    # While loop for countdown logic
    while seconds > 0:
        # For mins and secs count
        mins, secs = divmod(seconds, 60)

        # Time format variable MM:SS format
        time_format = '{:02d}:{:02d}'.format(mins, secs)

        # Output the formatted time, updating it on the same line
        print(time_format, end='\r')

        # Wait for 1 second
        time.sleep(1)

        # Decrease seconds
        seconds -= 1

    # Once time is up, print times up message
    print('00:00 \nTimes up!')

# User input for the timer
time_seconds = int(input('Enter time in seconds for countdown: '))

# Start the countdown timer with the input value
countdown_timer(time_seconds)



