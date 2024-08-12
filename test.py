A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2,3, 4], [1, 2, 3, 4]]

for i in range(4):
    for j in range(4):
        for k in range(4):
            A[i][j] += A[i][k] * A[k][j]
            A[i][j] = A[i][j] % 1000

print(A)