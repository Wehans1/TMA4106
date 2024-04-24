import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def funk(k, h):
    u = np.zeros((int(1/k), 10)) + 20
    
    for i in range(len(u[0])):
        u[0, i] = -i**2 + 278
    
    u[:, 0] = 0
    u[:, -1] = 0
    
    for i in range(1, len(u)-1):
        for j in range(1, len(u[i])-1):  # Iterate over columns up to len(u[i])-2
            if np.isnan(u[i+1, j]):
                u[i, j+1] = 0
            elif np.isnan(u[i-1, j]):
                u[i, j+1] = 0
            else:
                u[i, j] = k/2*h**2 * (u[i+1, j+1] - 2*u[i, j] + u[i-1, j+1]) +(k/2*h**2 * (u[i+1, j] - 2*u[i, j] + u[i-1, j])) + u[i, j]
    
    return u

# Generate data
k_val = 0.1
h_val = 0.6
u = funk(k_val, h_val)

# Create grid for 3D plot
x = np.arange(0, 10)
y = np.arange(0, len(u))
x, y = np.meshgrid(x, y)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, u, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
ax.set_title('3D Plot of the Function')
plt.show()
