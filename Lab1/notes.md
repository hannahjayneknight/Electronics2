## Exercise 1: Sinusoidal signal generation

*Files:* sine_gen.m, sine_gen_test.fig, sine_gen_test.png <br />

*What:* Made a function that generates a sine wave. Inputs: amplitude amp, frequency f, sampling frequency fs and duration T. <br />

Function finds the sampling time period to make an array from 0 to T with a gap of sampling time period. <br />

*Test:* A 400Hz sine wave was drawn with an amplitude of 1.

## Exercise 2: Spectrum of the signal

*Files:* plot_spec.m, plot_spec_test.fig, plot_spec_test.png <br />

*What:* Made a function that generates a frequency spectrum of a signal. Inputs: an array containing the data points of the signal sig and sampling frequency fs. <br />

Function uses the inbuilt MATLAB function fft to compute the frequency spectrum. This computes the discrete Fourier transform (DFT) of X using a fast Fourier transform (FFT) algorithm. <br />

*Test:* The sinewave from exercise 1 was plotted using a frequency domain.
