import math
a, b = int(input()), int(input())

for i in range(b+1):
    print(i, int(math.pow(a, i)))