# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        display.show(Image.YES)
        pin0.write_analog(40)
    elif button_b.was_pressed():
        display.show(Image.NO)
        pin0.write_analog(130)