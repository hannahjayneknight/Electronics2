## Setup

The wires for the battery pack needed to be connected by unscrewing the green thing shown below.


<img src="setting_up_lab5.jpg" alt="Setting up"/>
<img src="connecting_battery_pack.jpg" alt="Connecting the battery pack"/> 

## Exercise 1: DC Motor and H-bridge

*Files:* lab5task1a.py, lab5task1b.py <br />

The motors were connected and a python script was used to turn them. _lab5task1a.py_ is a script that can be used to determine which motor is motor A as it only turns on this motor. <br />

_lab5task1b.py_ uses the potentiometer to change the speed of the motor. PuTTY was used to connect to the PyBench and read the value of the potentiometer using the following lines of code. ```value``` gives a number from 0 to 4095 which is the range you get from 12 bits (ie 2^12).

```
pot = pyb.ADC(Pin(‘X11’))
value = pot.read()
```

Changing the speed did not happen instantaneously. The PyBench had to be reset for the motors speed to be visably changed and this was confirmed by also restarted PuTTY and re-reading the potentiometer value.

<img src="reading_potentiometer.jpg" alt="Reading the potentiometer using PuTTY"/> 

_lab5task1c.py_ displays the PWM duty cycle on the OLED display. This read a negative value when turning one way. It only got to a maximum motor drive of 99% in one direction and -99% in the other. The motors stopped turning at around 4%. Slightly above or below (12%) the motors would make a very high pitched noise without turning. <br />

_lab5task1c.py_ was edited to read the potentiometer value (0-4095) and display this underneath the motor drive on the OLED display. <br />

<img src="high_speed.jpg" alt="High speed"/> 
<img src="motors_off.jpg" alt="Motors off"/> 
<img src="reverse_direction.jpg" alt="Reverse direction"/> 

**General notes:**
- When connected to my laptop with the battery pack switched off, they turned. When the battery pack was switched on, they turned faster. When the PyBench was disconnected from my laptop with the battery pack still switched on, the continued spinning at the higher speed.
- There are two motors which are labelled A and B in the Python files.
- ```Pin.high()``` sets pin to “1” output level and ```Pin.low()``` sets pin to “0” output level. 
- We use an on-chip timer circuit inside the microcontroller to generate a 1000Hz PWM signal to drive the motor.
- 

**Notes on the timer circuit:**
- Each motor has two pins which are used to control the direction the motor turns. Each timer consists of a counter that counts up at a certain rate. The rate at which it counts is the peripheral clock frequency (in Hz) divided by the timer prescaler. When the counter reaches the timer period it triggers an event, and the counter resets back to zero. By using the callback method, the timer event can call a Python function. For more information on pyb Timers please see: https://docs.micropython.org/en/latest/library/pyb.Timer.html 
-  All timer channels share the same underlying timer, which means that they share the same timer clock. For more information on the pyb channel timer methods please see: https://docs.micropython.org/en/latest/library/pyb.Timer.html?highlight=tim%20channel#pyb.Timer.channel


<img src="" alt=""/> 

Video of motor turning on: <br />

