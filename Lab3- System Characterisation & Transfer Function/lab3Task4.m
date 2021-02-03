%Lab 3 Task 4 - Transient behaviour of Bulb Box

clear all

clf

ports = serialportlist;

pb = PyBench(ports(end)); % create a PyBench object

%set various parameters

fs = 100;

pb = pb.set_samp_freq(fs);

x_min = 1.0;

x_max = 1.5;

N = 500; %no of data samples

%Capture step response

pb.dc(x_min);

pause(1);

pb.dc(x_max)

rise = pb.get_block(N);

pb.dc(x_min)

fall = pb.get_block(N);

data = [rise' fall']

%plotting

clf

plot(data)

xlabel('Sample number');

ylabel('Output (V)');

title('Step Response - Experimental');