## Exercise 1: Sinusoidal signal generation

**Files:** sine_gen.m, sine_gen_test.fig, sine_gen_test.png <br />

**What:** Made a function that generates a sine wave. Inputs: amplitude amp, frequency f, sampling frequency fs and duration T. <br />

Function finds the sampling time period to make an array from 0 to T with a gap of sampling time period. <br />

**Test:** A 400Hz sine wave was drawn with an amplitude of 1.

## Exercise 2: Spectrum of the signal

**Files:** plot_spec.m, plot_spec_test.fig, plot_spec_test.png <br />

**What:** Made a function that generates a frequency spectrum of a signal. Inputs: an array containing the data points of the signal sig and sampling frequency fs. <br />

Function uses the inbuilt MATLAB function fft to compute the frequency spectrum. This computes the discrete Fourier transform (DFT) of X using a fast Fourier transform (FFT) algorithm. <br />

**Test:** The sinewave from exercise 1 was plotted using a frequency domain.

## Exercise 3: Two tones

**Files:**  combined_sine_wave.fig, combined_sine_wave.png, combined_sinewave_spectrum.fig, combined_sinewave_spectrum.png, combined_sine_wave_breakdown.jpg<br />

<br /> Two sine waves were generated: <br />
1. s1
    * f = 400Hz
    * amp = 1.0V
    * fs = 10k Hz
    * T = 1 sec 
2. s2
    * f = 1000Hz
    * amp = 0.5V
    * fs = 10k Hz
    * T = 1 sec 

<br /> These were then added together and plotted as a waveform (using MATLAB's plot function) and a spectrum (using my own plot_spec function). <br />

**Further notes:** The waveform looked like a squiggly line. I drew on the combined waveform to make the file combined_sine_wave_breakdown.jpg which shows s1 and s2. On the spectrum you can clearly see a line at 400Hz and 1000Hz which represent each waveform individually.


## Exercise 4: Two tones + noise

**Files:** noisy_wave.fig, noisy_wave.png<br />

**What:** MATLAB's randn() function was used to produce a set of random numbers and was added to the signal made in exercise 3. This was plotted as a wave and a spectrum. <br />

**Further notes:** Looking at the waveform alone, the amplitude of this wave varies enourmously from 1. Although a slight sine wave shape can be seen, it would have been nearly impossible to have inferred a sine wave from the noisy wave. This shows how noise can affect results and how important it is to minimise noise. <br />

However, when you look at the spectrum, the frequencies of the two main waves is clear as these have the greatest amplitude. The amplitude for all the remaining noise is less than 0.1. This shows how important it is to use both the waveform and the frequency spectrum when inferring a signal. Using the rough shape of the waveform tells us there are sine waves present and the frequency spectrum tells us the frequencies. 

## Exercise 5: Projection using dot product

**Files:**  <br />

**What:** The dot product of different signal combinations was found using:<br />

dot_product = v1*transpose(v2)

<br /> Results: <br />

| vector 1 (v1) | vector 2 (v2) | result      |
|---------------|---------------|-------------|
| s1            | s2            | 1.8263e-13  |
| s1            | s3            | -9.8339e-11 |
| s1 + s2       | s1            | 5000        |

<br /> Note that s3 is a signal of frequency 401Hz and amplitude 0.5.

**Notes on results:**

## Further exploration

**Files:**  <br />

**What:** <br />

**Test:**
