# Lab 7 - Self balancing segway

The objectives for this task are to learn tips that will help us with our chosen assessed challenge. The biggest challenge on offer is to programme a minature, self-bancing, dancing segway. However, since we are short on time, it is not compulsory to go all the way.

## Tip 1 - From idle to running

In the _lab7.py_ file you can see what Peter Cheung recommended. This is to keep the segway in idle mode until the USR button is pressed and to display on the OLED screen what the segway is doing ie driving, dancing etc, outside of the main program.

## Tip 2 - Use the DIP switches

The _main.py_ file has been edited so that it is ready to be filled with commands (eg ```execfile('challenge_4.py')```). This will mean that the PyBench will automatically run a file, for example a dancing segway file, when the switches begin in this position.

## Tip 3 - Tips for a dancing segway

- You should store the dance move in a text file (ASCII format), read this file at the start of the program and store the moves in an array BEFORE the main program loop.
- Use the Python exception handlers ```try:``` and ```finally:```. 
    - The finally clause will execute as the last task before the try statement completes
    - The finally clause will run whether or not  the try clause has produced an exception.
    - More information: https://docs.python.org/3/tutorial/errors.html
- Sudo-code for a dancing segway can be found in the *dancing_segway.py* file.

## Tip 4 - Pitch angle estimation
Here is a function to estimate the pitch angle using a complementary filter. 

```
def pitch_estimate ( pitch, dt, alpha ):
    theta.imu.pitch()
    pitch_dot = imu.get_gy()
    pitch = alpha*(pitch+pitch_dot*dt) + (1-alpha)*theta
    return ( pitch, pitch_dot )
```

**From Peter:** dt is delta time, the time since the last reading in the program loop. You find dt with tic and pyb.millis(). Don’t forget to adjust dt to seconds in your equation.

## Tip 8 - reading from text files in python

Text files will be used to store the dancing steps. They can also be used to store tuned constants or calibrated offset pitch angles.

1. Open the text file.

```f = open (‘myfile.txt’, ‘r’)```

2. Read ASCII text or numbers.

```
value = float (f.read())    # read a floating point number stored as text

for line in f:
    print(line)             # print one line at a time in f until end-of-file
f.close()                   # close the file
```

## CHALLENGE 2

**What:** This task is to Combine what you have learned in lab 4 and 5 so that you can control the speed and direction of the motors by tilting the PyBench board. One motor controlled with pitch angle and the other with roll angle. You should display the speed of each motor (revolution per second) on the LED display alongside the angles.

**How:** 

1. _lab4task5.py_ shows two pendulums showing the raw pitch angle and the filtered pitch angel. This was edited to display the numerical pitch and roll angles that had both been passed through a complementary filter on the OLED screen. 

The roll angle seemed wrong as didn't show an angle close to 0 degrees in the neutral position and didn't get close to 90 degrees when perpendicular to the neutral. Using ```imu.roll()``` it was observed that the roll angle was constantly 15 degrees off. So this was edited to account for the offset.

However, the complementary filter uses ```imu.get_gx()``` and it is unknown what the error is in this???

2. _lab5task3.py_ accurately displays the speed of both motors using interrupts. However, it adjusts the speed of the motors according to the potentiometer. This was edited to adjust the speed of the motors according to the pitch angle. It was also edited so that the PyBench acts like a real segway so that when you lean forward, the motors drive forward and when you lean backwards the motors drive backwards.

It was decided to omit the roll angle since this does not seem to be measuring accurately - should I test this again and try to include it?

3. The OLED screen displays the speed of both motors and the pitch angle.

4. The _main.py_ file was edited so that _challenge2.py_ automatically runs when the dip switches are in the 010 (2) position (2).

## CHALLENGE 5

**What:** Make a PID controller to self-balance the segway. The control angle is the measured pitch angle and the aim is to maintain it at 0 degrees.

1. Tried writing my own PID controller in _challenge5-attempt1.py_. The K_p, K_d and K_i values were manually fine-tuned following the method setout in lectures, however, this was unsuccessful as the robot never found an oscillation point. 

2. A PID controller class was found online: https://github.com/ivmech/ivPID. 
