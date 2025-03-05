import time
from datetime import datetime
def validate_time_format(reminder_time):
    try:
        time.strptime(reminder_time, "%H:%M:%S")
        return True
    except ValueError:
        return False
def set_reminder():
    print("Welcome to the Simple Reminder App!")
    reminder_time = input("Enter the time for your reminder (HH:MM:SS): ")
    if not validate_time_format(reminder_time):
        print("Invalid time format. Please use HH:MM:SS format.")
        return
    reminder_message = input("Enter the reminder message: ")
    print(f"Reminder set for {reminder_time}.")
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == reminder_time:
            print(f"Reminder: {reminder_message}")
            break
        time.sleep(1)  
if __name__ == "__main__":
    set_reminder()
