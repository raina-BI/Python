import time

# Function definition
def countdown_timer(seconds):
    while seconds > 0:
        mins = seconds // 60  # Calculate minutes
        secs = seconds % 60  # Calculate seconds
        timer = f'{mins:02}:{secs:02}'  # Format as MM:SS
        print(timer, end='\r')  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    print("\nTime is up!")  # Notify when the countdown ends

# Input validation
try:
    seconds = int(input("Enter the time in seconds: "))
    if seconds > 0:
        countdown_timer(seconds)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input! Please enter an integer.")
