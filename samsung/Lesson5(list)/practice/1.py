# task 1
# size = int(input("insert size: "))
#
# list = []
# for i in range(size):
#     list.append(int(input("insert number: ")))
#
# print("Набор закончен")
# list.reverse()
# print(list)

n = int(input())
m = [int(i) for i in input().split()]
print(min(m), max(m))