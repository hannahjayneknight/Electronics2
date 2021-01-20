% Exercise 1: Sinusoidal signal generation

function [sig] = sine_gen(amp, f, fs, T)
    % Function to generate a sine wave of amplitude amp, frequency f, 
    % sampling frequency fs and duration T
    
    % example: signal = sine_gen(1.0, 440, 8800, 1)
    
    dt = 1/fs;
    t = 0:dt:T;
    sig = amp*sin(2*pi*f*t);
    

    