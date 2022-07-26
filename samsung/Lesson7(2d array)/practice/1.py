n,m = int(input()), int(input())
a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(i*10)
    a.append(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    print()
