from machine import Pin
from utime import sleep
import _thread

# Set the LED pin (usually GPIO2 for internal LED)
led = Pin(2, Pin.OUT)

def loop():
    while True:
        led.on()   # Turn the LED on
        sleep(0.1)   # Wait for 1 second
        led.off()  # Turn the LED off
        sleep(0.1)   # Wait for 1 second


_thread.start_new_thread(loop, ())


