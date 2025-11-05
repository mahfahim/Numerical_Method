import numpy as np 
import matplotlib.pyplot as plt 

def stochastic(x, y, m=0, b=0, learn_rate=0.01, epoc = 10000):
    n = len(y)
    for _ in range(epoc):
        for i in range(n):
            xi = x[i:i+1]
            yi = y[i:i+1]
            y_pred = m * xi + b
            
            dm = -2 * xi * ( yi - y_pred)
            db = -2 * ( yi - y_pred)
            
            m -= learn_rate * dm
            b -= learn_rate * db
            
    return m,b 

np.random.seed(0)
x = 2* np.random.rand(100,1)
y = 3 * x + 4 + np.random.randn(100,1)
m , b = stochastic(x, y)

print(f"Slop is {m}")
print(f"Intercept is {b}")

yy = m * x + b
plt.plot(x,yy)
plt.scatter(x,yy)
plt.title("Stochastic Gradient Descent")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()