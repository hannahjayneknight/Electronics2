% Lab 4 - Task 1c: 3D display of angles (not in lab sheet)
clear all
close('all')
ports = serialportlist;
pb = PyBench(ports(end));  % create a PyBench object
model = IMU_3D();  % create the IMU 3D visualisation object
N = 50;
tic;
gx_1 = 0; gy_1 = 0; 	% initialise gyro angles
fig1 = figure(1);
while true
    for i = 1:N
        [p, r] = pb.get_accel();
        [x, y, z] = pb.get_gyro();
        dt = toc;
        tic;
        pitch = p*180/pi;
        roll = r*180/pi;
        gx_1 = max(min(gx_1+x*dt,pi/2),-pi/2);
        gy_1 = max(min(gy_1+y*dt,pi/2),-pi/2);
        clf(fig1);
        subplot(2,1,1);
        model.draw(fig1, p, r, 'Accelerometer');
        subplot(2,1,2);
        model.draw(fig1, gy_1, gx_1, 'Gyroscope');
        pause(0.0001);
    end  % for

end  % while
