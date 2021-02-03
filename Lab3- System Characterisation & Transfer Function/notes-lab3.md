## Setup: Checking that the bulb board works

**Notes:** All went smoothly. <br />

<img src="setting-up-bulb-board.jpg" alt="Setting up the bulb board"/> <nobr>

## Exercise 1: DC Characteristic of the Bulb Board

**Files:** No files. Methods were typed into the command line on MATLAB. <br />

**What:**  Tested using MATLAB with the Bulb Board. This included using the ```pb.dc(voltage)``` method and the  ```pb.get_one()``` method. <br /> 

At first, the ```pb.get_one()``` method seemed to be returning all sorts of results. To control the test, the board was restarted and MATLAB was closed and reopened before each test of the method. This was repeated for ```pb.dc(0)``` and ```pb.dc(1.5)```. The results are shown below. <br />

| DC value (V) | Result 1 | Result 2 | Result 3 | Result 4 | Result 5 | Result 6 | Result 7 | Average |
|--------------|----------|----------|----------|----------|----------|----------|----------|---------|
| 1.5          | 24.2199  | 22.7721  | 22.7705  | 6.6645   | 25.0094  | 20.9199  | 20.5025  | 22.6990 |
| 0            | 3.3000   | 2.6812   | 3.5062   | 2.8875   | 3.0938   | 3.5062   | 3.3000   | 3.1821  |

<br /> 

 Note that before each measurement was made, I waited a few moments after setting the dc value. After a while, the ```pb.get_one()``` method was returning values close to 0 for both DC values (I think due to something within the circuit causing the photodetector to turn off). When this happened, the PyBoard and MATLAB were restarted.

**Notes:** The ```pb.get_one()``` method measures ```a_in```. <br />

## Exercise 2: