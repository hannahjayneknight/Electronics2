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

Come back to this once completed challenge 4.

## Tip 5 - PID controller

Come back to this once completed challenge 4.

## Tip 6 - Tuning the PID controller

Come back to this once completed challenge 4.

## Tip 7 - Pseudo-code for self-balancing, dancing segway

Come back to this once completed challenge 4.

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
