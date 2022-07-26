m = int(input())
a = [int(i) for i in input().split()]
cnt = 0
for i in range(len(a)-1):
    if a[i+1] > a[i]:
        print(a[i],end=" ")
        cnt +=1
print(cnt)