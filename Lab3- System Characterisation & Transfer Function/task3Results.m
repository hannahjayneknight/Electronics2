%plotting the results from task 3

G = [3.3354, 4.0847, 5.8250, 9.4343, 3.8188, 1.3213];
G_dB = [10.4631, 12.2232, 15.3058, 19.4942, 11.6386, 2.42];
freq = [1.0, 3.0, 4.0, 5.0, 7.0, 9.0];

plot(freq, G);
title('Manually finding the Frequency Response');
xlabel('Frequency');
ylabel('Gain');