'''    Marks the start of comment section
-------------------------------------------------------
Name: Editing Lab 4 Exercise 5 in preparation for the oral exam
Creator:  	Hannah Knight
Date:   	10 March 2021
Revision: 	1
-------------------------------------------------------
Measures the pitch and roll angle, passes them through a 
complementary filter and displays this on the OLED screen in 
degrees. 
-------------------------------------------------------
'''    
import pyb
from pyb import LED
from oled_938 import OLED_938
from mpu6050 import MPU6050

# Define LEDs
b_LED = LED(4)

# I2C connected to Y9, Y10 (I2C bus 2) and Y11 is reset low active
oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64,
                   external_vcc=False, i2c_devid=60)
oled.poweron()
oled.init_display()

# IMU connected to X9 and X10
imu = MPU6050(1, False)    	# Use I2C port 1 on Pyboard

def read_imu_pendulum(dt):
	global g_pitch
	alpha = 0.7    # larger = longer time constant
	pitch = int(imu.pitch())  # pitch mesaured using accelerometer
	g_pitch = alpha*(g_pitch + imu.get_gy()*dt*0.001) + (1-alpha)*pitch # derived pitch using gyro
	# show pendulums
	oled.clear()
	oled.line(96, 26, pitch, 24, 1) # function defined in the oled_938.py file: line(self,x,y,phi,d, state) -> Draws a line of lenght d from (x,y) at angle phi in degrees
	oled.line(32, 26, g_pitch, 24, 1) # g_pitch is more accurate
	oled.draw_text(0,0," Raw | PITCH |")
	oled.draw_text(83,0, "filtered")
	oled.display()

def read_imu(dt):
	# prints the pitch and roll angles to the screen
	# both have been passed through a complementary filter
	global g_pitch
	global g_roll
	alpha = 0.7    # larger = longer time constant
	pitch = int(imu.pitch())  # pitch mesaured using accelerometer - measured in degrees
	roll = int(imu.roll() + 15) # measured in degrees
	g_pitch = alpha*(g_pitch + imu.get_gy()*dt*0.001) + (1-alpha)*pitch # derived pitch using gyro
	g_roll = alpha*(g_roll + imu.get_gx()*dt*0.001) + (1-alpha)*roll
	# show text
	oled.clear()
	oled.draw_text(0,20,"Roll angle: {:.2f}".format(g_roll))
	oled.draw_text(0,40, "Pitch angle: {:.2f}".format(g_pitch))
	oled.draw_text(0,0, "(All measured in degrees)")
	oled.display()

g_pitch = 0
g_roll = 0 
tic = pyb.millis()		
while True:
	b_LED.toggle()
	toc = pyb.millis()
	read_imu(toc-tic)
	tic = pyb.millis()
