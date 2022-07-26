#1
a,b = int(input()), int(input())
res = []
for i in range(1,b+1):
    res.append(pow(a,i))
print(res)

#2
not_unique = [0, 5, 15, 2, 15, 5, 0, 7, 9, 7, 16, 9, 16, 5, 15]
for i in not_unique:
    if not_unique.count(i) == 1:
        print(i)
    else: 
        continue

#3 newlist = [expression for item in iterable if condition == True]
x = int(input())
res = [int(i*i) for i in range(x+1)]

# for i in range(x+1):
#     res.append(i*i)

print(res)

#4
i_have_tuple = (1, 5, 10, 'strange string', 5, 9, 12)
for i in i_have_tuple:
    if str(i) == i:
        print(i)

#5
x = int(input())
a = [int(i) for i in input().split()]
y = int(input())
print(a.count(y))

#6
numbers = (12, 36, 45, 85, 11, 96, 10, 74, 25, 37, 78, 0, 12, 5)
res = 0
for i in numbers:
    res += i
print(res // len(numbers))