import numpy as np

# Example system: 3x3 augmented matrix [A|b]
arr = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]

main_array = np.array(arr, dtype=float)

# Separate coefficients matrix and last column
D = main_array[:, :-1]  # Coefficient matrix
last_col = main_array[:, -1]  # RHS vector

# Construct matrices for Cramer's Rule
D1 = np.column_stack((last_col, D[:, 1], D[:, 2]))  # Replace 1st column with b
D2 = np.column_stack((D[:, 0], last_col, D[:, 2]))  # Replace 2nd column with b
D3 = np.column_stack((D[:, 0], D[:, 1], last_col))  # Replace 3rd column with b

# Compute determinants
D_det = np.linalg.det(D)
D1_det = np.linalg.det(D1)
D2_det = np.linalg.det(D2)
D3_det = np.linalg.det(D3)

# Compute solutions
x = D1_det / D_det
y = D2_det / D_det
z = D3_det / D_det

print("x =", x)
print("y =", y)
print("z =", z)
