n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
l = 0
m = int(n / 2)
for i in range(m):
    a[l],a[m+1] = a[m+1],a[l]
    l += 1
    m += 1
    
print("-----------------------")

for i in a:
    for j in i:
        print(j, end = " ")
    print()