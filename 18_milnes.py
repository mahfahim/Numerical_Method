import numpy as np

def f(x, y):
    return x + y

# Values obtained previously (e.g., Picard / RK4 / Any method for 4 initial points)
# Example:
x_vals = [0, 0.1, 0.2, 0.3]
y_vals = [1.0, 1.1053, 1.2229, 1.3552]

x0, y0 = x_vals[0], y_vals[0]
x1, y1 = x_vals[1], y_vals[1]
x2, y2 = x_vals[2], y_vals[2]
x3, y3 = x_vals[3], y_vals[3]

def milne_method(x0, y0, x1, y1, x2, y2, x3, y3, h=0.1):
    y4_pred = y0 + (4*h/3)*(2*f(x3,y3) - f(x2,y2) + 2*f(x1,y1))
    y4_corr = y2 + (h/3)*(f(x2,y2) + 4*f(x3,y3) + f(x3+h, y4_pred))
    return y4_corr

y4 = milne_method(x0,y0,x1,y1,x2,y2,x3,y3)
print("Predicted y4 =", y4)
