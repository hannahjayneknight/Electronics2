clear all
% NB:  For these computer stored waveforms, fs = 44100.
[sig, fs] = audioread('two_drums.wav');
sound(sig, fs);
%plot the signal
figure(1);
clf;
plot(sig);
xlabel('Sample no');
ylabel('Signal (v)');
title('Two Drums');

split = buffer(sig, 300); % splits signal into 20 ms sections
energy  = split.^2;
sum_energy = sum(split.^2);

plot(sum_energy);
hold on
xlabel('Sample no');
ylabel('Energy of signal');
title('Two drums energy');

%Find local maxima
[pks locs] = findpeaks(sum_energy);
plot(locs, pks, 'o');
hold off
