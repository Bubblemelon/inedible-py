from gpiozero import LED
from time import sleep

led = LED(17)

# simple script that will cause an LED 
# connected to GPIO #17 to blink every 1 second

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)