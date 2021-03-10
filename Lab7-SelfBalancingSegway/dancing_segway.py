import pyb
from pyb import Pin, Timer, ADC, DAC, LED
import micropython
micropython.alloc_emergency_exception_buf(100)

# Initialise various peripherals e.g. OLED, IMU etc

# Initialise different constants, variables, arrays etc

# Read the dancing steps from file into array

# Wait for USR switch pressed

tic = pyb.millis()      # mark time now in msec

try:
    while True:
        if buffer is full, detect beat
        if beat detected, do next dance move

finally:
    motor.A_stop()
    motor.B_stop()