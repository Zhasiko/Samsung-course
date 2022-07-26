a = [int(i) for i in input().split()]
a.reverse()
r = a.copy()
sum = 0

for i in range(len(a)):
    if a[i] == 0:
        ind1 = i
        a.pop(a[i])
        break
for i in range(len(a)):
    if a[i] == 0:
        ind2 = i
        break

for i in range(ind1,ind2):
    sum += r[i+1]
print(sum)