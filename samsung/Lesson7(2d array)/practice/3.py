m, n = int(input()), int(input())
k = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
for i in range(m):
    print(a[i][k], end = " ")