n,m = int(input()), int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

s = []
for i in range(n):
    for j in range(m):
        if a[j][i] % 2 == 0:
            a[j][i] = 'x'
        s.append(a[j][i])
    if "x" in s:
        s.clear()
    else:
        print(i)
        exit()

print(0)