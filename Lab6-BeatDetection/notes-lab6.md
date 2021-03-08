##  Exercise 1: Moving Average filter

*Files:* lab6task1a.m, lab6task1b.m <br />

**What:** The MATLAB file _lab6task1a.m_ adds noise to a music sample, then uses a moving average filter to attempt to remove that noise. <br />

**Results:** When playing back the music sample for which the moving average filter had been applied, noise clearly still existed in the file, however, the amount of noise had been reduced. <br />

**Moving average filter:** Takes N number of samples of input at point in time and takes the average of those to make one output. For example, the formula for the ouput of a 4-point moving average filter would look like the following: <br />

<img src="4-point-moving-average.jpg" alt="4-point moving average formula"/>

Since averaging reduces the effect of fast changes, this is essentially a lowpass filter. <br />

**Change the variable for the number of taps:** The MATLAB file _lab6task1b.m_ was run multiple times, each time increasing the number of taps by 5. The number of taps was tested in the range 5-50 plus an additional measurement at N = 100. <br />

Increasing the number of taps certainly reduced the amount of noise that remained in the music file sample, however, it also meant that the volume of the music file was reduced, too. <br />

The biggest drop in noise was noticed when the number of taps was increased from 15 to 20. <br />

Whilst the amount of noise had reduced for N = 100, it had not all disappeared. Furthermore, the main music sample was even quieter. <br />

However, it is worth noting that it is difficult to measure how much noise remains solely by listening. This experiment would be more accurate if there was a more accurate method of measuring the signal-to-noise ratio.