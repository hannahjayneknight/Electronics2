import time
import pyb
from pyb import Pin, Timer, ADC, ExtInt
from mpu6050 import MPU6050
from oled_938 import OLED_938
import PID


"""
Setup
"""

oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64, external_vcc=False, i2c_devid=60)
oled.poweron()
oled.init_display()
print('Performing Challenge 5')
print('Waiting for button press') # for debugging
trigger = pyb.Switch()      # create trigger switch object
while not trigger():        # wait for trigger pressed
    time.sleep(0.001)
while trigger(): pass       # wait for release
print('Button pressed - tuning the PID control.')

imu = MPU6050(1, False)
pot = ADC(Pin('X11'))
A1 = Pin('X3', Pin.OUT_PP)
A2 = Pin('X4', Pin.OUT_PP)
PWMA = Pin('X1')
B1 = Pin('X7', Pin.OUT_PP)
B2 = Pin('X8', Pin.OUT_PP)
PWMB = Pin('X2')
tim = Timer(2, freq=1000)
motor_a = tim.channel(1, Timer.PWM, pin=PWMA)
motor_b = tim.channel(2, Timer.PWM, pin=PWMB)


"""
Functions we need
"""

def read_imu(dt, alpha):
	# prints the pitch and roll angles to the screen
	# both have been passed through a complementary filter
	global g_pitch
	pitch = int(imu.pitch())  # pitch mesaured using accelerometer - measured in degrees
    pitch_dot = int(imu.get_gy())
	g_pitch = alpha*(g_pitch + imu.get_gy()*dt*0.001) + (1-alpha)*pitch # derived pitch using gyro
    return g_pitch, pitch_dot

def forward(motor, pin1, pin2, speed):
    """ Function to set the motors moving forward """
    pin1.low()
    pin2.high()
    motor.pulse_width_percent(speed)

def backward(motor, pin1, pin2, speed):
    """ Function to set the motors moving backward """
    pin1.high()
    pin2.low()
    motor.pulse_width_percent(speed)

def stop(pin1, pin2):
    """ Function to stop the motors """
    pin1.high()
    pin2.high()


"""
Initialize variables
"""

error = 0 # feedback
pid.SetPoint=0.0
pid.setSampleTime(5)
alpha_val = 0.9
P = 0.5
I = 0
D = 0
pid = PID.PID(P, I, D)
feedback_list = []
time_list = []
setpoint_list = []

"""
Program loop
"""

try:
    tic1 = pyb.micros()
    while True:
        dt_val = pyb.micros() - tic1
        if dt_val > 5000:
            p, p_dot = read_imu(dt_val, alpha_val)
            tic1 += dt_val

finally:
    stop(A2, A1)
    stop(B1, B2)
