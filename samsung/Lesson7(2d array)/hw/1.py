n,m = int(input()), int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

for i in range(len(a)):
    print(max(a[i]))