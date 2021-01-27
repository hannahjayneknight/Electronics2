
clear all
ports = serialportlist;
pb = PyBench(ports(end));

%fprintf(pb.usb, '%s\n', 'S')
%fread(pb.usb, 1)

pb.set_sig_freq(440);
pb.set_samp_freq(8000);
pb.set_max_v(3.0);
pb.set_min_v(0.5);
pb.set_duty_cycle(50);
pb.sine();


