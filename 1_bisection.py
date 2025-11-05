import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 2

def bisection(f, a, b, tot=1e-5):
    
    if f(a) * f(b) >= 0:
      raise ValueError("f(a) and f(b) will be opposite sign")
    
    mid = (a + b) / 2.0
    
    if abs(f(mid)) < tot:
        return mid

    elif f(a) * f(mid) < 0 :
        return bisection(f , a , mid , tot)
    
    else:
        return bisection(f , mid , b , tot)
    

root = bisection(f,0,10,1e-5)
print(f"The root is {root}")

x = np.arange(0,3,0.1)
y = f(x)

plt.plot(x,y,label="f(x) = x^2 - 2")
plt.title("Bisection Method")
plt.scatter(root, f(root), color='blue')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

