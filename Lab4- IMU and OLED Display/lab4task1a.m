clear all
close('all')
ports = serialportlist;
pb = PyBench(ports(end));
N = 500;
end_time = 10.0;
while true
    figure(1)
    clf(1)
    axis([0 end_time -90 90]);
    title('Accelerometer: Pitch & Roll Angles', 'FontSize', 16);
    ylabel('Angles (deg)', 'FontSize', 14);
    grid on; hold on;
    tic;
    % read and plot accelerometer data
    for i = 1:N
        [p, r] = pb.get_accel(); % in radians
        timestamp = toc;
        pitch = p*180/pi; % convert to derees
        roll = r*180/pi;
        plot(timestamp, pitch, '.b'); % plot pitch in blue
        plot(timestamp, roll, '.r'); % plot roll in red
        pause(0.001); % 1 ms
    end
    end_time = toc; %use actual time range from now on
    
end