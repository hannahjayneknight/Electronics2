clear all;
ports = serialportlist;     % find all serial ports
pb = PyBench(ports(end));   % create a PyBench object with the last port

% Set sampling frquency
fs = 8000;
pb = pb.set_samp_freq(fs);

% Capture N samples
N = 1000;
samples = pb.get_mic(1000);
data = samples - mean(samples); % remove dc offset

% plot data
figure(1);
clf
plot(data);
xlabel('Sample no');
ylabel('Signal voltage (V) ');
title('Microphone signal');

% Find and plot spectrum
figure(2);
plot_spec(data, fs)
















