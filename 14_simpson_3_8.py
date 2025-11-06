import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Sample function to integrate
def fun(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

# Simpson's 3/8 rule implementation
def simpsons_3_8_rule(fun, a, b):
    a, b = min(a, b), max(a, b)
    h = (b - a) / 3
    return (3 * h / 8) * (fun(a) + 3 * fun(a + h) + 3 * fun(a + 2 * h) + fun(b))

# Plotting the function
array = np.arange(-0.01, 0.82, 0.01)
plt.plot(array, fun(array), label="f(x)")

# Define points for the 3/8 rule
a, b, c, d = 0, 0.8/3, 0.8/3*2, 0.8

# Calculate and print the result
result = simpsons_3_8_rule(fun, a, d)
print("Simpson's 3/8 rule ->", result)

# Plot the Simpson's 3/8 rule approximation
plt.scatter([a, b, c, d], [fun(a), fun(b), fun(c), fun(d)], color='green')
plt.plot(array, CubicSpline([a, b, c, d], [fun(a), fun(b), fun(c), fun(d)])(array), '--', color='blue', label="Simpson's 3/8 rule")
plt.fill_between(array, CubicSpline([a, b, c, d], [fun(a), fun(b), fun(c), fun(d)])(array), alpha=0.3)
plt.legend()
plt.show()
