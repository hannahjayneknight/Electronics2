clear all;
ports = serialportlist;
pb = PyBench(ports(end));

x_dc = linspace(0, 2, 15);
y_dc = zeros(length(x_dc), 1);

for i = 1:length(x_dc)
    pb.dc(x_dc(i)); % set the dc value
    pause(5); 
    y_dc(i) = pb.get_one();
    
    
end

pb.dc(0); % turning the bulb off as measurements have been taken

plot(x_dc, y_dc);
title('Measuring the DC characteristic of the Bulb Board system');
xlabel('x_dc');
ylabel('y_dc');
