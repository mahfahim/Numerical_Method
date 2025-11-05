import numpy as np 

def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(f"{arr[i][j]:0.2f}", end=" ")
        print()

def gause_elimination(row,col,arr):
    
    for i in range(row):
        for j in range(col):
            if i == j:
                cof = arr[i][j]
                for k in range(j, col+1, 1):
                    arr[i][k] = float(arr[i][k]/cof)
                for p in range(i+1,row,1):
                    cof2 = arr[p][i]
                    for q in range(col+1):
                        arr[p][q] = arr[p][q] - cof2 * arr[i][q]
    
    for i in range(row-1,-1,-1):
        
        for j in range(col-1,-1,-1):
            
    
arr =[ [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]  ]

gause_elimination(3,3,arr)

print_arr(arr)





                    