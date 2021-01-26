clear all
ports = serialportlist;     % find all serial ports
pb = PyBench(ports(end));   % create a PyBench object with the last port

% setting parameters

f = 440;                    % signal frequency
fs = 8000;                  % sampling frequency
pb = pb.set_sig_freq(f);
pb = pb.set_samp_freq(fs);
pb = pb.set_max_v(3.0);     % set maximum output voltage
pb = pb.set_min_v(0.5);     % set minimum output voltage
pb = pb.set_duty_cycle(50);

% generate signal

pb.sine();
% pb.triangle();
% pb.square();


