import numpy as np
import matplotlib.pyplot as plt

# Approximations
def Y1(x):
    return 1 + x + x**2 / 2

def Y2(x):
    return 1 + x + x**2 / 2 + x**3 / 3 + x**4 / 8

def Y3(x):
    return 1 + x + x**2/2 + x**3/3 + x**4/8 + x**5/15 + x**6/48

def picard_method(f, x0, h=0.1, n=10):
    x_values = np.arange(x0, x0 + n*h, h)
    y_values = np.array([f(x) for x in x_values])
    return x_values, y_values

x_values, y_values = picard_method(Y3, 0, 0.1, 10)

plt.plot(x_values, y_values)
plt.title("Picard's Method Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
