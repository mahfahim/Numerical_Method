import numpy as np


def gradient_descent(x, y, m=0, b=0, lrn_rate=0.01, epoc=1000):
    n = len(x)
    for _ in range(epoc):
        y_pred = m*x + b
        
        dm = -(2/n) * sum(x * (y - y_pred))
        db = -(2/n) * sum((y - y_pred))
        
        m -= (lrn_rate * dm)
        b -= (lrn_rate * db)
    
    return m,b

np.random.seed(0)

x = np.random.rand(100,1)
y = 5 * x + 3 + np.random.randn(100,1)

m,b = gradient_descent(x, y)

print(f"Slope is {m}")
print(f"Intercept is {b}")
