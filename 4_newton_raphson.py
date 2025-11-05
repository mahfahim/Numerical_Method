import numpy as np
import matplotlib.pyplot as plt 

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

def newton_raphson(f, df, x, max_iter=100, tol=1e-5):
    
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new    
        x = x_new
    
    print("this is not converge")

root = newton_raphson(f, df, 1)
print(f"The root is {root}")
    
x = np.arange(-10,10,0.1)
y = f(x)
plt.plot(x, y, label="f(x)=x**2 - 2")
plt.scatter(root,f(root),color="blue")
plt.title("Newton raphson method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
    
    
    