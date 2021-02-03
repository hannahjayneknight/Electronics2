## Setup: Checking that the bulb board works

**Notes:** All went smoothly. <br />

<img src="setting-up-bulb-board.jpg" alt="Setting up the bulb board"/>

## Exercise 1: DC Characteristic of the Bulb Board

1. Initial testing of using MATLAB with the Bulb Board. <br /> 

*Files:* No files. Methods were typed into the command line on MATLAB. <br />

This included using the ```pb.dc(voltage)``` method and the  ```pb.get_one()``` method. <br /> 

At first, the ```pb.get_one()``` method seemed to be returning all sorts of results. To control the test, the board was restarted and MATLAB was closed and reopened before each test of the method. This was repeated for ```pb.dc(0)``` and ```pb.dc(1.5)```. The results are shown below. <br />

| DC value (V) | Result 1 | Result 2 | Result 3 | Result 4 | Result 5 | Result 6 | Result 7 | Average |
|--------------|----------|----------|----------|----------|----------|----------|----------|---------|
| 1.5          | 24.2199  | 22.7721  | 22.7705  | 6.6645   | 25.0094  | 20.9199  | 20.5025  | 22.6990 |
| 0            | 3.3000   | 2.6812   | 3.5062   | 2.8875   | 3.0938   | 3.5062   | 3.3000   | 3.1821  |

<br /> 

 Note that before each measurement was made, I waited a few moments after setting the dc value. After a while, the ```pb.get_one()``` method was returning values close to 0 for both DC values (I think due to something within the circuit causing the photodetector to turn off). When this happened, the PyBoard and MATLAB were restarted. <br /> 

2. Finding the maximum and minimum voltage values for the bulb to light <br />

Filament starts to glow red at 0.3V = x_dcl <br />
Brightness doesn't increase any further after 1.7V = x_dch <br />

| x_dc | y_dc    |
|------|---------|
| 0.3  | 2.0456  |
| 1.7  | 48.6823 |

3. Writing a MATLAB file to find the ```a_in``` values for a range of inputted DC values. Then,  a graph of x_dc can be plotted against y_dc to see the relationship. <br />

*Files:* lab3Task1.m, DC-characteristics-bulb-board.fig <br />

What we're putting in is a voltage, and we're getting light intensity out. <br />

The results show an initial linear section as the bulb heats up, followed by quadratic relationship (Determined by the formula P=V^2/R. In this case V is the inputted DC value and P is the light intensity). followed by a linear section when the bulb is fully heated. The final linear region is for x_dc values at 1.7V or higher - so my initial prediction for the max value for x_dc was correct! <br /> 

<img src="DC-characteristics-bulb-board.png" alt="DC characteristic of bulb board"/>

4. Optional task

(To be completed later) <br />

**Notes:** The ```pb.get_one()``` method measures ```a_in```. <br />

## Exercise 2: Frequency Response of the Bulb Board system - Simulation

*Files:* lab3Task2.m, theoretical-freq-response.fig,  <br />

We find and plot the theoretical frequency repsonse of the bulb board. <br />

**Explanation of the code:** COME BACK TO THIS <br />

<img src="theoretical-freq-response.png" alt="Theoretical frequency respons"/> 

## Exercise 3: Measure the Frequency Response of the Bulb Board system using PyBench

*Files:* lab3Task2.m, theoretical-freq-response.fig,  <br />
