class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def display_times(self):
        print(f'{self.hours:02d}:{self.minutes:02d}')
class AnalogClock(Clock):
    def display_times(self):
        super().display_times()

class DigitalClock(Clock):
    def display_times(self):
        super().display_times()

analog_clock = AnalogClock(1, 45)
digital_clock = DigitalClock(15, 43)
analog_clock.display_times()
digital_clock.display_times()