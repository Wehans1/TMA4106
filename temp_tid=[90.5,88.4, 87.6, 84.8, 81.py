import matplotlib.pyplot as plt
import numpy as np


temp_tid = [90.5, 89.4, 87.6, 84.8, 81.9, 79.0, 76.2, 73.3, 70.5, 68.2, 65.8, 63.7, 61.5, 59.5, 57.8, 56.2, 54.4, 53.1, 51.5, 50.2, 49.0, 47.8, 47.7, 46.8, 45.9, 44.8]
time_intervals = np.arange(0, len(temp_tid), 1)
T = []
alpha = 0.0445
for t in range(26):
    b = 21.0 + (90.5 - 21.0) * np.exp(-alpha * t)
    T.append(b)


plt.figure(figsize=(10, 6))
plt.plot(time_intervals, temp_tid, marker='o', linestyle='-', color='orange', label='Observert temperature')
plt.plot(range(26), T, marker='o', linestyle='-', color='b', label='Teoretisk Temperature')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature vs. Time')
plt.grid(True)
plt.legend()

plt.show()

print (T)
