n = int(input())
m = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
sum = 0

for i in range(n):
    for j in range(m):
        sum += a[j][i]
    print(sum, end = " ")
    sum = 0