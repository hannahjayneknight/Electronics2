%Lab 4 - Task 1b: testing the gyroscope
clear all
close('all')
ports = serialportlist;
pb = PyBench(ports(end));
N = 500; %each graph is 500 time points
end_time =10.0; %initial guess of time axis range(10sec)
gx = 0; gy = 0; %initialise angles gy pitch, gx roll

while true
    %plot the axes frist for plot later
    figure(1)
    clf(1)
    axis([0 end_time -90 90]); %fix axes scaling btw +-90
    title('Gyroscope: Pitch & Roll Angles', 'FontSize', 16);
    xlabel('Angles(Deg)', 'FontSize', 14);
    ylabel('Time(sec)', 'FontSize', 14);
    grid on; hold on; %overlay plotting on same axes scaling
    timestamp = 0;
    tic; %define start time
    %read and plot accelerometer data
    for i = 1:N
        [x, y, z] = pb.get_gyro(); %get angular rate in rad/s
        dt = toc; %get elapsed time since last tic
        tic;
        timestamp = timestamp + dt
        gx = max(min(gx+x*dt, pi/2), -pi/2); %limit to +/- pi/2, Accumulate gx and gy
        gy = max(min(gy+y*dt, pi/2), -pi/2);
        plot(timestamp, gy*180/pi, '.b'); %plot pitch in blue
        plot(timestamp, gx*180/pi, '.r'); %plot roll in red
        pause(0.001); %delay 1 sec
    end
    end_time = timestamp; %use actual time range from now on
end
