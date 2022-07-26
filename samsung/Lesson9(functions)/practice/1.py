def sol(n,a):
    a[0] = a[n-1]
    return a
            
n,m = int(input()), int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

print(sol(n,a))