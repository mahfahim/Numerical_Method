import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Define the backward interpolation method
def backward(x, y, x_n):
    # Calculate the backward differences
    arr = [y]
    for i in range(3):  # You can increase this for higher order differences
        temp = []
        for j in range(0, len(arr[-1])-1):
            temp.append(arr[-1][j] - arr[-1][j+1])
        arr.append(temp)
    print("Backward differences:", arr)

    # Calculate the interpolation value at x_n
    h = (x_n - x[-1]) / (x[1] - x[0])
    a = arr[0][-1]
    b = h * arr[1][-1]
    c = h * (h+1) / 2 * arr[2][-1]
    d = h * (h+1) * (h+2) / 6 * arr[3][-1]

    return a + b + c + d

# Data points
x = [1, 2, 3, 4]
y = [1, 8, 27, 64]
x_n = 2.5  # Point to interpolate

# Calculate the interpolated value
y_n = backward(x, y, x_n)

# Use cubic spline interpolation for visualization
x, y = np.array(x), np.array(y)
fn = interp1d(x, y, kind='cubic')
x_new = np.linspace(x.min(), x.max(), 100)
y_new = fn(x_new)

# Plotting
plt.plot(x_new, y_new, label='Cubic Spline', color='green')
plt.plot(x, y, color='red', label='Data Points')
plt.scatter(x_n, y_n, color='blue', label='Interpolated Point')
plt.title('Backward Interpolation Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
