import numpy as np 
import matplotlib.pyplot as plt 

def sigmoid_function(x):
    return 1/(1 + np.exp(-x))

def logistic_regression(x, m, b):
    z = m * x + b
    return sigmoid_function(z)

x_input = float(input("Enter a float number x : "))
m = float(input("Input a float number m : "))
b = float(input("Input a float number b : "))

probability = logistic_regression(x_input, m, b)

print(f"The probability of   {x_input} is : {probability}")

x = np.linspace(-10, 10, 100)
y = sigmoid_function(x)

plt.plot(x,y)
plt.title("Logistic Regression")
plt.scatter(x_input, probability , color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()