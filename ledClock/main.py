from machine import Pin
from neopixel import NeoPixel
import time
from clock import Clock
from display import *

pin1 = Pin(0, Pin.OUT)
np1 = NeoPixel(pin1, 12)
pin2 = Pin(4, Pin.OUT)
np2 = NeoPixel(pin2, 24)

clock = Clock(2)

while True:
    tim = clock.currentTime()
    displayHM(np1, tim)
    displayS(np2, tim)
    print(tim)
    time.sleep(1)

