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
