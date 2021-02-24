'''
-------------------------------------------------------
Name: User's own program for Lab 5 Task 1a
Creator: Hannah Knight
Date: 24/02/2021
-------------------------------------------------------
A python script to run motor A only.
-------------------------------------------------------
'''
import pyb
from pyb import Pin, Timer

# Define pins to control motor
A1 = Pin('X3', Pin.OUT_PP)		# Control direction of motor A
A2 = Pin('X4', Pin.OUT_PP)
PWMA = Pin('X1')				# Control speed of motor A

# Configure timer 2 to produce 1KHz clock for PWM control
tim = Timer(2, freq = 1000) # creating a timer object
motorA = tim.channel (1, Timer.PWM, pin = PWMA) # creating a channel obj

def A_forward(value):
	A1.low()
	A2.high()
	motorA.pulse_width_percent(value) # using a method within the .channel() class

def A_back(value):
	A2.low()
	A1.high()
	motorA.pulse_width_percent(value)
	
def A_stop():
	A1.high()
	A2.high()
	
A_forward(50)