'''
-------------------------------------------------------
Name: Lab 7
Creator:  Hannah j Knight
Date:   10 March 2021
Revision:  1
-------------------------------------------------------
'''
import pyb
from pyb import Pin, Timer, ADC, DAC, LED
from array import array
from oled_938 import OLED_938

oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64,
                   external_vcc=False, i2c_devid=60)
oled.poweron()
oled.init_display()
oled.draw_text(0,0, 'Hannah J Knight')
oled.draw_text(0,10, 'Milestone 1: Driving')
oled.draw_text(0,20, 'Press USR button')
oled.display()

print('Performing Milestone 1') # these are to help with debugging as will show up on PuTTY
print('Waiting for button press')
trigger = pyb.Switch()
while not trigger(): # wait for trigger to be pressed
    time.sleep(0.001)

while trigger(): pass # wait for release
print('Button pressed - Running')