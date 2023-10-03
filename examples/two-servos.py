# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        display.show('1')
        pin1.write_analog(40)
        sleep(500)    # edit the number in the brackets to control the timing
        pin1.write_analog(130)
        sleep(500)    # edit the number in the brackets to control the timing
    elif button_b.was_pressed():
        display.show('2')
        pin2.write_analog(40)
        sleep(500)    # edit the number in the brackets to control the timing
        pin2.write_analog(130)
        sleep(500)    # edit the number in the brackets to control the timing
