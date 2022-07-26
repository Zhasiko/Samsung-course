#1
a = int(input())
if a > 0:
    a = a+1
elif a < 0:
    a = a - 2
else:
    a = 10
print(a)

#2
a = int(input())
b = int(input())
if a != b:
    a = a + b
    b = a + b
elif a == b:
    a = 0
    b = 0
print(a,b)

#3

l = input()
if l == 'a' or 'e' or 'e' or 'o' or 'u':
    print("Vowel")
else:
    print("Constant")

#4
a,b = int(input()),int(input())
print(min(a,b))

#5

a = int(input())
if a in range(10,20):
    print("YES")
else:
    print("NO")

#6

a = int(input())
if a >= 0:
    a +=1
else:
    a = a
print(a)

#7
a = int(input())
if a % 2 == 0:
    print("EVEN")
else:
    print("ODD")

#8
def is_leap(year):
    leap = False
    
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        leap = True
    
    return leap
year = int(input())
print(is_leap(year))