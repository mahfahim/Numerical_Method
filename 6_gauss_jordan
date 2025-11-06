import copy

def print_arr(arr):
    for row in arr:
        print(row)

def gauss_jordan(arr, N):
    arr = copy.deepcopy(arr)  # make a copy to avoid modifying original

    for i in range(N):
        # Make the diagonal element 1 by dividing the row
        diag = arr[i][i]
        for k in range(N+1):
            arr[i][k] /= diag

        # Make all other elements in column i zero
        for j in range(N):
            if i != j:
                factor = arr[j][i]
                for k in range(N+1):
                    arr[j][k] -= arr[i][k] * factor

        print("Step", i+1)
        print_arr(arr)
        print()

    # Solution is the last column
    print("Solution:")
    for i in range(N):
        print(arr[i][N])


# Example run
N = 3
arr = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

gauss_jordan(arr, N)
