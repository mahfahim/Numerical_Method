import copy

def print_arr(arr):
    for row in arr:
        print(row)

def gaussian_elimination(N, arr):
    arr = copy.deepcopy(arr)

    # Forward Elimination
    for i in range(N):
        # Make the diagonal element 1
        pivot = arr[i][i]
        for j in range(N, -1, -1):
            arr[i][j] /= pivot

        # Eliminate below
        for j in range(i+1, N):
            factor = arr[j][i]
            for k in range(N, -1, -1):
                arr[j][k] -= factor * arr[i][k]

        print_arr(arr)
        print()

    # Back Substitution
    solve = [0 for _ in range(N)]
    for i in range(N-1, -1, -1):
        solve[i] = arr[i][N]
        for k in range(i+1, N):
            solve[i] -= arr[i][k] * solve[k]
        solve[i] /= arr[i][i]

    print("Solution:", solve)

# Example run:
N = 3
arr = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

gaussian_elimination(N, arr)
