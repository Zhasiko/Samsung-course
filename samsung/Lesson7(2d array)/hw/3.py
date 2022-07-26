n,m = int(input()), int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

for i in range(0,n,2):
    print(a[i],":",sum(a[i])/m)