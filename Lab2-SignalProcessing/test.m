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