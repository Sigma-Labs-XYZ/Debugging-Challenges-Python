# A class based Alarm clock simulator
# Do not edit this code, the aim is to debug!

from datetime import datetime, timedelta, date
import time

class AlarmClock:
    """A simple alarm clock class."""

    def __init__(self, alarm_time: str) -> None:
    """
    Initialize a new alarm clock instance.

    Args:
        alarm_time: A string representing the time that the alarm should go off, in the format "HH:MM:SS".
    """
    self.alarm_time = datetime.strptime(alarm_time, "%H:%M:%S %d/%m/%Y")

    def set_alarm(self, alarm_time: str) -> None:
        """
        Set the time for the alarm to go off.

        Args:
            alarm_time: A string representing the time that the alarm should go off, in the format "HH:MM:SS".
        """
        self.alarm_time = datetime.strptime(alarm_time, "%H:%M:%S %d/%m/%Y")

    def check_alarm(self) -> bool:
        """
        Check if the current time has passed the alarm time.

        Returns:
            A boolean indicating whether the current time has passed the alarm time.
        """
        current_time = datetime.now().time()
        current_time = datetime.combine(datetime.today(), current_time)
        return current_time >= self.alarm_time

    def time_until_alarm(self) -> timedelta:
        """
        Get the amount of time until the alarm goes off.

        Returns:
            A timedelta object representing the amount of time until the alarm goes off.
        """
        current_time = datetime.now().time()
        current_time = datetime.combine(datetime.today(), current_time)
        if current_time >= self.alarm_time:
            self.alarm_time += timedelta(days=1) 
        return alarm_time - current_time


if __name__ == "__main__":
    # Create a new alarm clock instance with an initial alarm time of 5 seconds from now
    timestamp_to_set = datetime.now() + timedelta(seconds=5)
    alarm_clock = AlarmClock(timestamp_to_set.strftime("%H:%M:%S %d/%m/%Y"))

    # Wait until the alarm time is reached
    while alarm_clock.check_alarm():
        time_until_alarm = alarm_clock.time_until_alarm()
        print(f"Alarm goes off in {time_until_alarm.seconds} seconds")
        time.sleep(1)

    # Alarm time has been reached, sound the alarm
    print("ALARM!") 
