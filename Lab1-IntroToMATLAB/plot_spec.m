function plot_spec(sig, fs)

    % Function to plot frequency spectrum of signal.
    
    % example: plot_spectrum(sig, 1000)
    
    magnitude = abs(fft(sig)); %MATLAB inbuilt function fft computes the frquency spectrum
    N = length(sig);
    df = fs/N;
    f = 0:df:(fs/2);
    Y = magnitude(1:length(f));
    plot(f, 2*Y/N)
    xlabel('\fontsize{14}Frequency (Hz)'); 
    ylabel('\fontsize{14}Magnitude'); 
    title('\fontsize{16}Spectrum');