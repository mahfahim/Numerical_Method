import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x + 1

def g(x):
    return (x**3 + 1) / 4

def iteration(g, x, max_iter=100, tol=1e-5):
    
    for i in range(max_iter):
         x_new = g(x)
         
         if abs(x_new - x) < tol:
             return x_new
         
         x = x_new
    
    # raise ValueError("Iteration does not converge within the max iteration")
    print("Iteration does not converge within the max iteration")

root = iteration(g, 1)
print(f"The root is {root}")

x = np.arange(-10, 10, 0.1)
y = g(x)
plt.plot(x, y, label="f(x) = x^3 - 4x + 1")
plt.scatter(root, g(root), color="blue")
plt.title("Iteration method")
plt.xlabel("x")
plt.ylabel("g(x) = (x^3 + 1) / 4")
plt.legend()
plt.grid()
plt.show()