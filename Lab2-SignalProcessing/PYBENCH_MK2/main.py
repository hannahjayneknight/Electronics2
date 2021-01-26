'''
-------------------------------------------------------
Name: main
Creator:  Peter Y K Cheung, Imperial College London
Date:   29 Nov 2020
Revision: 1.0
-------------------------------------------------------
This is the main program to test the bulb board
DIP switch configuration

SW = 0  Run user.py
SW = 5  Run bulb_board_test.py
SW = 6  Run pybench_test.py
SW = 7  Run pybench_main.py
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
from pyb import Pin, LED

#  Configure X2:4, X7 as setting input pin - pull_up to receive switch settings
s0=Pin('Y8',pyb.Pin.IN,pyb.Pin.PULL_UP)
s1=Pin('Y3',pyb.Pin.IN,pyb.Pin.PULL_UP)
s2=Pin('X6',pyb.Pin.IN,pyb.Pin.PULL_UP)
r_LED = LED(1)
g_LED = LED(2)
y_LED = LED(3)
b_LED = LED(4)
'''f
Define various test functions
'''
def read_sw():
	value = 7 - (s0.value() + 2*s1.value() + 4*s2.value())
	return value

if read_sw() == 0:
    print('Run User Program')
    execfile('user.py')
elif read_sw() == 5:
	print('Running bulb board test')
	execfile('bulb_test.py')
elif read_sw() == 6:
	print('Running PyBench Selftest')
	execfile('pybench_test.py')	
elif read_sw() == 7:
    print('Running PyBench')
    execfile('pybench_main.py')