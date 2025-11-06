import numpy as np 
import matplotlib.pyplot as plt

def polynomial(x, y, a=0, b=0, c=0, lrn_rate=0.01, epoc=1000):
    n = len(y)
    for _ in range(epoc):
        y_pred = a * x**2 + b * x + c
        
        da = -2/n * sum((y - y_pred)* x**2)
        db = -2/n * sum((y -y_pred)* x)
        dc = -2/n * sum(y - y_pred)
        
        a -= lrn_rate * da
        b -= lrn_rate * db
        c -= lrn_rate * dc
        
    return a, b, c

np.random.seed(0)
x = np.random.rand(100,1)
y = 4 * x**2 + 5 * x + 3 + np.random.randn(100,1)

a, b, c = polynomial(x, y)


print(f"a = {a}   b = {b}  c = {c}")

xx = np.linspace(0,1,100)
yy = a * xx**2 + b * xx + c

plt.plot(xx,yy)
plt.title("Polynomial regression")
plt.scatter(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
