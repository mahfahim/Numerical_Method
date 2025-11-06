import numpy as np
import matplotlib.pyplot as plt

# Sample function to integrate
def fun(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Trapezoidal rule implementation for n sub-intervals
def trapezoidal_rule(fun, a, b, n=100):
    x = np.linspace(a, b, n+1)   # n sub-intervals => n+1 points
    y = fun(x)
    h = (b - a) / n
    return h * (0.5*y[0] + y[1:-1].sum() + 0.5*y[-1])

# Interval and number of sub-intervals
a, b = 0, 0.8
n = 8  # You can increase n for better accuracy

# Calculate integral
result = trapezoidal_rule(fun, a, b, n)
print("Trapezoidal rule approximation:", result)

# Plot the function
x_vals = np.linspace(-0.01, 0.82, 100)
plt.plot(x_vals, fun(x_vals), label='f(x)')

# Plot trapezoids
x_trap = np.linspace(a, b, n+1)
y_trap = fun(x_trap)
for i in range(n):
    plt.fill_between([x_trap[i], x_trap[i+1]], [y_trap[i], y_trap[i+1]], color='red', alpha=0.3)

# Plot trapezoid top lines
plt.plot(x_trap, y_trap, color='red', label='Trapezoidal approximation')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Trapezoidal Rule Approximation')
plt.legend()
plt.grid(True)
plt.show()
