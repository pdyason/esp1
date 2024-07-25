from machine import Pin
from time import sleep

# Set the LED pin (usually GPIO2 for internal LED)
led = Pin(2, Pin.OUT)

while True:
    led.on()   # Turn the LED on
    sleep(1)   # Wait for 1 second
    led.off()  # Turn the LED off
    sleep(1)   # Wait for 1 second
