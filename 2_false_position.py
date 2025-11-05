import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 -2

def false_position(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) will be oposite sign")
    
    c = a - ((b - a) * f(a)) / (f(b) - f(a)) 
    
    if abs(f(c)) < tol:
        return c
    
    elif f(a) * f(c) < 0:
        return false_position(f, a, c, tol)
    
    else:
        return false_position(f, c, b, tol)
    
    
root = false_position(f, 0, 10)

print(f"The root is {root}")
    
    
x = np.arange(0, 3, 0.1)
y = f(x)

plt.plot(x, y, label="f(x) = x^2 - 2")
plt.scatter(root,f(root),color="blue")
plt.title("False Postion Method")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.legend()
plt.grid()
plt.show()
