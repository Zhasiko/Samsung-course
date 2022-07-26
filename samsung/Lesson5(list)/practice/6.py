n = [int(i) for i in input('N = ').split()]
list = []
for i in n:
    list.append(n.count(i))
print(max(list))