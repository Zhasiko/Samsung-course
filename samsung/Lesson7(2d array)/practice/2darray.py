# #1
# a = []
# for i in range(3):
#     b = []
#     for j in range(3):
#         b.append(input())
#     a.append(b)
# print(a)

n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
print(a)