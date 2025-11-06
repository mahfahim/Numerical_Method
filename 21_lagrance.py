import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d  # Ensure this import is included

# Define the Lagrange interpolation method
def lagrange(x, y, x_n):
    n = len(x)
    res = 0
    for i in range(n):
        temp = y[i]
        for j in range(n):
            if i != j:
                temp *= (x_n - x[j])
                temp /= (x[i] - x[j])
        res += temp
    return res

# Data points
x = [1, 2, 3, 4]
y = [1, 8, 27, 64]
x_n = 2.5  # Point to interpolate

# Calculate the interpolated value using Lagrange method
y_n_lagrange = lagrange(x, y, x_n)
print(f"Lagrange Interpolated value at x = {x_n} is y = {y_n_lagrange}")

# Use cubic spline interpolation for visualization
x, y = np.array(x), np.array(y)
fn = interp1d(x, y, kind='cubic')
x_new = np.linspace(x.min(), x.max(), 100)
y_new = fn(x_new)

# Plotting
plt.plot(x_new, y_new, label='Cubic Spline', color='green')
plt.plot(x, y, color='red', label='Data Points')
plt.scatter(x_n, y_n_lagrange, color='blue', label='Lagrange Interpolated Point')
plt.title('Lagrange Interpolation Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
