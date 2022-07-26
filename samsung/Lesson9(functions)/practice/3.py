def mas(a,n):
    for i in range(len(a)):
        if i == a[i] and a[i] % n != 0:
            print(a[i])

a = [int(i) for i in input().split()]
n = int(input())

mas(a,n)