clear; clc; close all;

% Parameters
rho = 1.2;
C = 1;
E_true = 1000;

% Times
t = linspace(1,20,12);

% Exact blast radius
R_true = C * ((E_true .* t.^2 ./ rho)).^(1/5);

% Add 5% measurement noise
noise_level = 0.05;
R_obs = R_true .* (1 + noise_level*randn(size(R_true)));

% Log transform
x = log(t);
y = log(R_obs);

% Linear fit
p = polyfit(x,y,1);

slope_est = p(1);
intercept_est = p(2);

% Recover energy
E_est = rho * exp(5*intercept_est);

% Relative errors
slope_error = abs(slope_est-0.4)/0.4*100;
energy_error = abs(E_est-E_true)/E_true*100;

fprintf('Recovered slope = %.4f\n',slope_est);
fprintf('Recovered energy = %.2f\n',E_est);

fprintf('Slope error = %.2f %%\n',slope_error);
fprintf('Energy error = %.2f %%\n',energy_error);

% Plot
figure
scatter(x,y,60,'filled')
hold on

xfit = linspace(min(x),max(x),100);
yfit = polyval(p,xfit);

plot(xfit,yfit,'r','LineWidth',2)

xlabel('log(t)')
ylabel('log(R)')
title('Taylor blast-wave fit')
legend('Synthetic data','Linear fit','Location','best')

grid on

saveas(gcf,'blast_fit.png')