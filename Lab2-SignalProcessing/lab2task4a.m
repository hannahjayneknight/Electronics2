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
plot_spec_dB(data, fs);

% find spectrum and create a hamming window
figure(2);
plot_spec_dB(data, fs);
window = hamming(length(data));

while true
    samples = pb.get_mic(N);
    data = samples - mean(samples);
    clf;
    plot_spec_dB(data, fs);
    hold on
    plot_spec_dB(data.*window, fs);
end