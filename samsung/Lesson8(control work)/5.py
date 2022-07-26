n,m = int(input()), int(input())
k = int(input())

a = [[int(j) for j in input().split()] for i in range(n)]
a.pop(k)
print(a)
        