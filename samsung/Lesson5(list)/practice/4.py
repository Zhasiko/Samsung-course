a = [int(i) for i in input().split()]

for i in range(len(a)-1):
    if a[i+1] > a[i]:
        print(a[i],end = " ")
        exit()
print(0)