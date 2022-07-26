n = int(input())
matrix = [[1] * n for _ in range(n)]

for i in range(n):
    matrix[i][n - 1 - i] = 0
    for j in range(n):
        if i > n - 1 - j:
            matrix[i][j] = 2
        print(matrix[i][j], end=" ")
    print()