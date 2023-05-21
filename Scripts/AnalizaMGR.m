clear;clc;close all
%General avg times
bf_times = [0.01365, 0.23562, 5.57084, 152.91373, 191.97853];
dp_times = [0.01532, 0.03865, 0.13679, 0.25145, 0.33174];
ga_times = [0.661112, 0.81863, 0.90516, 1.182736, 5.11080];
sa_times = [0.0017249, 0.02338, 0.02525, 0.02394, 0.02346];
my_alg_times = [0.07393, 0.04365, 0.04716, 0.04907, 0.89026];
%No items
no_items = [15, 30, 50, 75, 100];
%Ratio
bf_ratio = [1, 1, 1, 1, 1];
dp_ratio = [1, 1, 1, 1, 1];
ga_ratio = [0.993086, 0.1863, 0.90516, 1.18273, 0.82353];
sa_ratio = [0.916324, 0.68028 ,0.41763, 0.40051, 0.02346, 0.34418];
my_alg_ratio = [0.8683128, 0.87738, 0.04716, 0.89026, 0.04842, 0.91701];
%Brute force best, weakness and avg times
bf_times_15 = [0.0079938, 0.0245826 , bf_times(1)];
bf_times_30 = [0.2422846, 0.2795901, bf_times(2)];
bf_times_50 = [5.5072916, 5.7080022, bf_times(3)];
bf_times_75 = [147.2210572, 176.1457903, bf_times(4)];
bf_times_100 = [191.2180644, 193.5552762 , bf_times(5)];
%Dynaming programming best, weakness and avg times
dp_times_15 = [0.0119974, 0.0220322, dp_times(1)];
dp_times_30 = [0.035088, 0.0408977, dp_times(2)];
dp_times_50 = [0.1295211, 0.1451773, dp_times(3)];
dp_times_75 = [0.3210701, 0.3906211, dp_times(4)];
dp_times_100 = [0.2389788, 0.309387, dp_times(5)];
%GA best, weakness and avg times
ga_times_15 = [0.0119974, 0.0220322, ga_times(1)];
ga_times_30 = [0.8016644, 0.8360597, ga_times(2)];
ga_times_50 = [1.1413462, 1.2115784, ga_times(3)];
ga_times_75 = [4.9600599, 5.5385969, ga_times(4)];
ga_times_100 = [6.0072858 ,6.146231, ga_times(5)];
%SA best, weakness and avg times
sa_times_15 = [0.02797, 0.036441, sa_times(1)];
sa_times_30 = [0.0215104, 0.0279962, sa_times(2)];
sa_times_50 = [0.0207129, 0.0343187, sa_times(3)];
sa_times_75 = [0.021607, 0.0310418, sa_times(4)];
sa_times_100 = [0.0127119, 0.033864, sa_times(5)];
%My own alg best, weakness and avg times
my_alg_times_15 = [0.073293, 0.074486, my_alg_times(1)];
my_alg_times_30 = [0.0429847, 0.0444095, my_alg_times(2)];
my_alg_times_50 = [0.0460195, 0.0482608, my_alg_times(3)];
my_alg_times_75 = [0.0462523, 0.0518304, my_alg_times(4)];
my_alg_times_100 = [0.0468827, 0.0499289, my_alg_times(5)];
figure(1)
subplot(2,2,1);
x_p1 = no_items;
y_p1 = bf_times;
bar(x_p1, y_p1);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack times with differents no items Brute force');
subplot(2,2,2);
y_p2 = [bf_times_15, bf_times_30 ,bf_times_50, bf_times_75 ,bf_times_100];
x_p2 = [no_items(1), no_items(1) + 3, no_items(1) + 6, no_items(2), no_items(2) + 3, no_items(2) + 6, no_items(3) , no_items(3) + 3, no_items(3) + 6, no_items(4), no_items(4) + 3, no_items(4) + 6, no_items(5), no_items(5) + 3, no_items(5) + 6];
bar(x_p2, y_p2);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack best, weakness and average times Brute force');
figure(2)
subplot(2,2,1);
x_p1 = no_items;
y_p1 = dp_times;
bar(x_p1, y_p1);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack times with differents no items Dynamic Programming');
subplot(2,2,2);
y_p2 = [dp_times_15, dp_times_30 ,dp_times_50, dp_times_75 ,dp_times_100];
x_p2 = [no_items(1), no_items(1) + 3, no_items(1) + 6, no_items(2), no_items(2) + 3, no_items(2) + 6, no_items(3) , no_items(3) + 3, no_items(3) + 6, no_items(4), no_items(4) + 3, no_items(4) + 6, no_items(5), no_items(5) + 3, no_items(5) + 6];
bar(x_p2, y_p2);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack best, weakness and average times Dynamic Programming');
figure(3)
subplot(2,2,1);
x_p1 = no_items
y_p1 = ga_times
bar(x_p1, y_p1);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack times with differents no items GA');
subplot(2,2,2);
y_p2 = [ga_times_15, ga_times_30 ,ga_times_50, ga_times_75 ,ga_times_100];
x_p2 = [no_items(1), no_items(1) + 3, no_items(1) + 6, no_items(2), no_items(2) + 3, no_items(2) + 6, no_items(3) , no_items(3) + 3, no_items(3) + 6, no_items(4), no_items(4) + 3, no_items(4) + 6, no_items(5), no_items(5) + 3, no_items(5) + 6];
bar(x_p2, y_p2);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack best, weakness and average times GA');
figure(4)
subplot(2,2,1);
x_p1 = no_items;
y_p1 = sa_times;
bar(x_p1, y_p1);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack times with differents no items SA');
subplot(2,2,2);
y_p2 = [sa_times_15, sa_times_30 ,sa_times_50, sa_times_75 ,sa_times_100];
x_p2 = [no_items(1), no_items(1) + 3, no_items(1) + 6, no_items(2), no_items(2) + 3, no_items(2) + 6, no_items(3) , no_items(3) + 3, no_items(3) + 6, no_items(4), no_items(4) + 3, no_items(4) + 6, no_items(5), no_items(5) + 3, no_items(5) + 6];
bar(x_p2, y_p2);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack best, weakness and average times SA');
figure(5)
subplot(2,2,1);
x_p1 = no_items;
y_p1 = my_alg_times;
bar(x_p1, y_p1);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title("Solving knapsack times with differents no items Author's algortihm");
subplot(2,2,2);
y_p2 = [my_alg_times_15, my_alg_times_30 ,my_alg_times_50, my_alg_times_75 ,my_alg_times_100];
x_p2 = [no_items(1), no_items(1) + 3, no_items(1) + 6, no_items(2), no_items(2) + 3, no_items(2) + 6, no_items(3) , no_items(3) + 3, no_items(3) + 6, no_items(4), no_items(4) + 3, no_items(4) + 6, no_items(5), no_items(5) + 3, no_items(5) + 6];
bar(x_p2, y_p2);
grid on;
xlabel('No Items in knapsack [n]');
ylabel('Time to solve knapsack [s]');
title('Solving knapsack best, weakness and average times SA');