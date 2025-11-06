import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Sample function to integrate
def fun(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

# Simpson's 1/3 rule implementation
def simpsons_1_3_rule(fun, a, b):
    return (b - a) / 6 * (fun(a) + 4 * fun((a + b) / 2) + fun(b))

# Plotting the function
array = np.arange(-0.01, 0.82, 0.01)
plt.plot(array, fun(array), label="f(x)")

# Calculate and print the result
result = simpsons_1_3_rule(fun, 0, 0.8)
print("Simpson's 1/3 rule ->", result)

# Plot the Simpson's 1/3 rule approximation
plt.scatter([0, 0.4, 0.8], [fun(0), fun(0.4), fun(0.8)], color='green')
plt.plot(array, CubicSpline([0, 0.4, 0.8], [fun(0), fun(0.4), fun(0.8)])(array), '--', color='red', label="Simpson's 1/3 rule")
plt.fill_between(array, CubicSpline([0, 0.4, 0.8], [fun(0), fun(0.4), fun(0.8)])(array), color='red', alpha=0.3)
plt.legend()
plt.show()
