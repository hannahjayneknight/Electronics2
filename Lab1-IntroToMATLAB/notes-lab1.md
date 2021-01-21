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

**Further notes:** The waveform looked like a squiggly line. I drew on the combined waveform to make the file combined_sine_wave_breakdown.jpg which shows s1 and s2. On the spectrum you can clearly see a line at 400Hz and 1000Hz which represent each waveform individually. A useful tool to quickly see the effect of combining sine waves: https://demonstrations.wolfram.com/CombiningSineWaves/


## Exercise 4: Two tones + noise

**Files:** noisy_wave.fig, noisy_wave.png<br />

**What:** MATLAB's randn() function was used to produce a set of random numbers and was added to the signal made in exercise 3. This was plotted as a wave and a spectrum. <br />

**Further notes:** Looking at the waveform alone, the amplitude of this wave varies enourmously from 1. Although a slight sine wave shape can be seen, it would have been nearly impossible to have inferred a sine wave from the noisy wave. This shows how noise can affect results and how important it is to minimise noise. <br />

However, when you look at the spectrum, the frequencies of the two main waves is clear as these have the greatest amplitude. The amplitude for all the remaining noise is less than 0.1. This shows how important it is to use both the waveform and the frequency spectrum when inferring a signal. Using the rough shape of the waveform tells us there are sine waves present and the frequency spectrum tells us the frequencies. 

## Exercise 5: Projection using dot product

**Files:**  None <br />

**What:** The dot product of different signal combinations was found using: <br />

dot_product = v1*transpose(v2)

<br /> Results: <br />

| vector 1 (v1) | vector 2 (v2) | result      |
|---------------|---------------|-------------|
| s1            | s2            | 1.8263e-13  |
| s1            | s3            | -9.8339e-11 |
| s1 + s2       | s1            | 5000        |

<br /> Note that s3 is a signal of frequency 401Hz and amplitude 0.5.

**Notes on results:** Finding the dot product of two signsls tells us how much they have in common (ie how similar they are). A positive dot product means that two signals have a lot in common, meanwhile, a negative dot product means that the signals are related in a negative way, like vectors pointing in opposing directions. <br />

This means that signals s1 and s2 are strongly related, meanwhile, signals s1 and s2 or s1 and s3 are not strongly related at all as their dot product is close to 0.

## Further exploration

**Files:** analysing_phase_shift.fig, analysing_phase_shift.png <br />

**What:** *Analysing phase shift* Firstly, the sine_gen function was edited to take in another argument: phase, inputted as phi. This means that the function can be used to generate a sine wave with a phase shift. Two new versions of s1 and s2 were made with the same properties as before, but s1 had a phase shift of 0 radians and s2 had a phase shift of pi radians. The waveform made in exercise three could then be compared to this one. As expected, the waveform produced in this exercise had the same shape but was shifted to the left by half a cycle, or had a phase shift of pi. <br />

Note that whenever you add two sinewaves, they could have different frequencies, different phase shifts or both, we use the trigonometric addition rule to combine them and find the new frequency. Source: http://spiff.rit.edu/classes/phys207/lectures/beats/add_beats.html
