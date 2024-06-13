import datetime
import time

def set_alarm():
    alarm_time = input("Enter the time for the alarm in HH:MM format: ")
    alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    return alarm_hour, alarm_minute

def check_alarm(alarm_hour, alarm_minute):
    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        
        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Alarm! Wake up!")
            break
        time.sleep(1)  # Wait for 1 second before checking the time again

def main():
    print("Welcome to the Simple Alarm Clock!")
    alarm_hour, alarm_minute = set_alarm()
    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}.")
    check_alarm(alarm_hour, alarm_minute)

if __name__ == "__main__":
    main()
