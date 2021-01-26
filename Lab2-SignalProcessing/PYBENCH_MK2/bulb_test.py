'''
-------------------------------------------------------
Name: calibrate.py
Creator:  Peter Y K Cheung, Imperial College London
Date:   3 March 2017
Revision: 1.1
-------------------------------------------------------
This output a dc voltage on DAC and measure the voltage from ADC
User adjusts the trimpot to achieve dc calibration
-------------------------------------------------------
The MIT License (MIT)
Copyright (c) 2014 Sebastian Plamauer, oeplse@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''	

import pyb
import math
import gc
from pyb import LED, USB_VCP, DAC, Timer, ADC, Pin, UART
from array import array
from oled_938 import OLED_938

# Define various ports, pins and peripherals
a_out = DAC(1, bits=12)
a_in = ADC(Pin('X12'))
r_LED = LED(1)
g_LED = LED(2)
y_LED = LED(3)
b_LED = LED(4)

# I2C connected to Y9, Y10 (I2C bus 2) and Y11 is reset low active
i2c = pyb.I2C(2, pyb.I2C.MASTER)
devid = i2c.scan()
oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64,
                   external_vcc=False, i2c_devid=i2c.scan()[0])
oled.poweron()
oled.init_display()

def sw_released():
    while sw.value() == True:
        pass        # wait for release
    return

sw = pyb.Switch()
data_array = array('H', 0 for i in range(128))  # reserve space for data array
vmax = 1.5
vmin = 0.8

def	plot_sig(signal,message):
	index = len(signal)
	if index >= 128:
		step = min(index,int(index/128))
	else:
		step = 1
	oled.clear()
	oled.draw_text(0,0,message)
	x = 127
	max_sig = max(max(signal),3000)
	min_sig = min(min(signal),1000)
	range_sig = max_sig - min_sig
	for i in range(0,index,step):
		y = 63 - int((signal[i] - min_sig)*55/range_sig)
		oled.set_pixel(x,y,True)
		x = x - 1
	oled.display()

# Loop to adjust trimpot
while True:
    vout = 1.5
    a_out.write(int(vout*4096/3.3))
    while sw.value() == False:
        light_level = 3.3*(a_in.read()/4096)
        oled.clear()
        oled.draw_text(0,0,"Adjust pot for 1.5V")
        oled.draw_text(0,20,'Brightness: {:5.2f}V'.format(light_level))
        oled.display()
        pyb.delay(100)

# Perform transient test
    sw_released()

    oled.clear()
    oled.draw_text(0, 0, "Transient Test")
    oled.draw_text(0, 20, 'Brightness oscillates')
    oled.display()

    tic = pyb.millis()

# loop to test transient behaviour
    while sw.value() == False:
        # step up
        a_out.write(int(vmax * 4096 / 3.3))
        a_in.read_timed(data_array, pyb.Timer(6, freq=100))
        while  (pyb.millis() - tic)<2000:
            toc = pyb.millis()
            # do nothing
        tic = pyb.millis()
        plot_sig(data_array, "+ve Step Response")

        # step down
        a_out.write(int(vmin * 4096 / 3.3))
        a_in.read_timed(data_array, pyb.Timer(6, freq=100))
        while  (pyb.millis() - tic)<2000:
            toc = pyb.millis()
        # do nothing
        tic = pyb.millis()
        plot_sig(data_array, "-ve Step Response")
    sw_released()