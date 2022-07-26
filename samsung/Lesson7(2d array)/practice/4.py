n,m = int(input()), int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] < 0:
            a[i][j] = "x"
            cnt += 1
            
print(cnt)

for i in range(n):
    for j in range(m):
        print(a[i][j],end = " ")
    print()