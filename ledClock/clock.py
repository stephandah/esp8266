from machine import RTC
from ntptime import settime

class Clock:
    def __init__(self, offset):
        self.offset = offset
        self.rtc = RTC()
        self.setTime()

    def currentTime(self):
        y, m, d, wd, H, M, S, ms = self.rtc.datetime()
        tzH = (H + self.offset) % 24
        return (tzH, M, S)

    def setTime(self):
        settime()
