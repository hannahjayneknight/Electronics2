import time
import micropython      # Needed for interrupt
import pyb
from pyb import Pin, Timer, ADC
from mpu6050 import MPU6050
from oled_938 import OLED_938  # Use OLED display driver
# OLED screen setup
oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64, external_vcc=False, i2c_devid=60)
oled.poweron()
oled.init_display()

##
# Code for running code only on USR button press
##
oled.draw_text(0, 0, 'Hannah Knight')
oled.draw_text(0, 10, 'Challenge 5')
oled.draw_text(0, 20, 'Press USR button')
oled.display()
print('Performing Challenge 5')
print('Waiting for button press')
trigger = pyb.Switch()      # create trigger switch object
while not trigger():        # wait for trigger pressed
    time.sleep(0.001)
while trigger(): pass       # wait for release
print('Button pressed - tuning the PID control.')

##
# Code to create peripheral objects and interrupts
##
# Start interrupt
micropython.alloc_emergency_exception_buf(100)
# IMU device
imu = MPU6050(1, False)
pot = ADC(Pin('X11'))           # 5k ohm potentiometer to ADC input on pin X11
# Define pins to control motor
A1 = Pin('X3', Pin.OUT_PP)      # Control direction of motor A
A2 = Pin('X4', Pin.OUT_PP)
PWMA = Pin('X1')                # Control speed of motor A
B1 = Pin('X7', Pin.OUT_PP)      # Control direction of motor B
B2 = Pin('X8', Pin.OUT_PP)
PWMB = Pin('X2')                # Control speed of motor B
# Configure timer 2 to produce 1kHz clock for PWM control
tim = Timer(2, freq=1000)
motor_a = tim.channel(1, Timer.PWM, pin=PWMA)
motor_b = tim.channel(2, Timer.PWM, pin=PWMB)

##
# Code for pitch calculation and PID control
##

def clamp(var, min_var, max_var):
    """ Function to clamp variables to a range """
    if var < min_var:
        return min_var
    elif var > max_var:
        return max_var
    else:
        return var

def pitch_estimate(pitch, dt, alpha):
    """ Function to calculate pitch angle using complementary filter """
    theta = imu.pitch()
    pitch_dot = imu.get_gy()
    pitch = alpha * (pitch + pitch_dot * dt * 0.001) + (1-alpha) * theta
    return pitch, pitch_dot

def read_imu(dt):
	# prints the pitch and roll angles to the screen
	# both have been passed through a complementary filter
	global g_pitch
	alpha = 0.7    # larger = longer time constant
	pitch = int(imu.pitch())  # pitch mesaured using accelerometer - measured in degrees
	g_pitch = alpha*(g_pitch + imu.get_gy()*dt*0.001) + (1-alpha)*pitch # derived pitch using gyro

def pid_controller(pitch, pitch_dot, target, integral, dt):
    """ Function to compute the PID control"""
    K_p = 4
    K_d = 0
    K_i = 0
    clamp(target, -3, 3)
    # integral term
    integral += (setpoint - p) * K_i
    integral = clamp(integral, 3000, -3000) # limit wind up
    # Compute the output W as sum of P, I, D terms
    w = K_p * (target - pitch) + K_d * ((target - pitch) - previous_error) + integral 
    # Limit pwm_value to +- 100
    w = clamp(w, -100, 100)
    return w

##
# Code for motor control
##
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


# Define input parameters
init_pitch = 0
previous_error = 0
setpoint = 0
integral = 0
alpha_val = 0.9
# tic2 = pyb.millis() for beat detection 
try:
    tic1 = pyb.micros()
    while True:
        dt_val = pyb.micros() - tic1
        if dt_val > 5000:
            p, p_dot = pitch_estimate(init_pitch, dt_val, alpha_val) # estimate pitch angle and pitch_dot
            #print("Pitch angle: {:5.2f}".format(p))
            #print("Rate of change of pitch angle: {:5.2f}".format(p_dot))
            tic1 += dt_val # update tic1
            pwm_value = pid_controller(p, p_dot, setpoint, integral, dt_val) # PID control
            previous_error = setpoint - p
            #print("pitch_error: {:5.2f}".format(pitch_error))
            #print("integral: {:5.2f}".format(integral))
            new_speed = 2 * pwm_value    # use returned value to move motor
            print("PWM value: {:5.2f}".format(pwm_value))
            if (p > 90 or p < -90): # stop the motors if we're far from vertical and there's no chance of success
                stop(A2, A1)
                stop(B1, B2)
            if new_speed <= -10:
                forward(motor_a, A2, A1, new_speed)
                forward(motor_b, B1, B2, new_speed)
            elif new_speed >= 10:
                backward(motor_a, A2, A1, new_speed) 
                backward(motor_b, B1, B2, new_speed) 
            else:  # stop motors
                stop(A2, A1)
                stop(B1, B2)
finally:  # always executed if exception
    # stop motors
    stop(A2, A1)
    stop(B1, B2)