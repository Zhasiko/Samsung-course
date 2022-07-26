a = [int(i) for i in input().split()]
b = filter(lambda x: x > 0,a)
c = filter(lambda y: y < 0,a)
print([len(list(b)),sum(list(c))])