%Lab 3 Task 2 - Plot theoretical freq. response of Bulb Board

f = (0:0.1:20);

D = [0.038 1.19 43 1000];     % specify denominator

s = 1i*2*pi*f;                % s = jw (1i is sqrt(-1))

G = 1000./abs(polyval(D,s));  %polynomial evaluation

Gdb = 20*log10(G);            % Gain in dB

figure;

plot(f,Gdb);

xlabel('Frequency (Hz)');

ylabel('Gain (db)');

title('Frequency Response - Theoretical');