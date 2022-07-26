# n = int(input())
# l = [int(input()) for _ in range(n)]
# m = int(input())
# if m in l:
#     print('Yes', 'Index:', l.index(m))

a = [int(i) for i in input().split()]
m = int(input())

for i in range(len(a)):
    if m == a[i]:
        print("YES, index:", i)
        exit()
print("NO")
