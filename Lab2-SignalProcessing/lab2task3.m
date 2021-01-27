clear all;
ports = serialportlist;
pb = PyBench(ports(end));

pb.set_samp_freq(8000);
N = 1000;
samples = pb.get_mic(N);
data = samples - mean(samples); % remove dc offset

% plot data
figure(1);
clf
plot(data);
xlabel('Sample no');
ylabel('Signal voltage (V)');
title('Microphone signal');

% find and plot spectrum
figure(2);
plot_spec(data, fs);
