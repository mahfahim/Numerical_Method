import numpy as np
import matplotlib.pyplot as plt

# Differential equation dy/dx = x + y
def f(x, y):
    return x + y

# Euler's Method
def euler_method(f, x0, y0, h=0.1, n=100):
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        
        x_values.append(x0)
        y_values.append(y0)
    
    return np.array(x_values), np.array(y_values)

# Initial Values
x0 = 0
y0 = 1
h = 0.1
n = 100

x_values, y_values = euler_method(f, x0, y0, h, n)

plt.plot(x_values, y_values, label="Euler's Method", color='blue')
plt.title("Euler's Method for Solving ODE")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()
