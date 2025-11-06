import numpy as np
import matplotlib.pyplot as plt

def polynomial_gradient_descent(x, y, a=0, b=0, c=0, lrn_rate=0.01, epoc=2000):
    n = len(x)
    for _ in range(epoc):
        y_pred = a*(x**2) + b*x + c
        
        da = -(2/n) * sum((y - y_pred) * (x**2))
        db = -(2/n) * sum((y - y_pred) * x)
        dc = -(2/n) * sum((y - y_pred))

        a -= lrn_rate * da
        b -= lrn_rate * db
        c -= lrn_rate * dc
    
    return a, b, c

# Data Generation (not perfectly linear now)
np.random.seed(0)
x = np.random.rand(100,1)
y = 4*(x**2) + 5*x + 3 + np.random.randn(100,1)   # real polynomial

# Train Model
a, b, c = polynomial_gradient_descent(x, y)

print(f"a (x^2 coefficient) = {a}")
print(f"b (x coefficient) = {b}")
print(f"c (intercept) = {c}")

# Plot
plt.scatter(x, y)

# Sort x for smooth curve
x_curve = np.linspace(0,1,100).reshape(-1,1)
y_curve = a*(x_curve**2) + b*x_curve + c

plt.plot(x_curve, y_curve, color="red")
plt.title("Polynomial Regression (Gradient Descent)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
