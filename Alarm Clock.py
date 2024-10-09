from playsound import playsound
import time

CLEAR = "\033[2J"  # Corrected clear screen sequence
CLEAR_AND_RETURN = "\033[H"  # Moves the cursor back to the top-left

def alarm(seconds):
    """
    Runs a countdown timer and plays an alarm sound when the time is up.

    Args:
        seconds (int): The total number of seconds to count down from.
    """
    time_elapsed = 0
    print(CLEAR)

    # Countdown loop
    while time_elapsed < seconds:
        time.sleep(1)  # Wait for 1 second
        time_elapsed += 1

        # Calculate the time remaining
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  
        seconds_left = time_left % 60

        # Print remaining time in MM:SS format, flushing the output to update in place
        print(f"{CLEAR_AND_RETURN}Time remaining: {minutes_left:02d}:{seconds_left:02d}", flush=True)

    # Play the alarm sound when time is up
    playsound("mixkit-digital-clock-digital-alarm-buzzer-992.wav")


if __name__ == "__main__":
    # Prompt the user for input time in minutes and seconds
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds  # Convert total time to seconds

    alarm(total_seconds)  # Start the alarm
