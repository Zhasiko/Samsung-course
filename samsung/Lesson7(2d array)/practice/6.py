n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = "x"
            
for i in range(n):
    for j in range(n):
        print(a[i][j], end =" ")
    print()