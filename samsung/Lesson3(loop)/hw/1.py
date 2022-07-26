#1
log = input()
pas = input()
if log == "admin" and pas == "my_super_secure_password":
    print('Welcome, admin!')
else:
    print("Don’t try,bad guy!")

#2
a, b = int(input()), int(input())
if a > b:
    print(1)
else:
    print(-1)

#3
def is_leap(year):
    leap = False
    
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        leap = True
    
    return leap
year = int(input())
print(is_leap(year))

#4
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#5
a = int(input("cost: "))
b = input("choose: dollar, euro, rouble: ")
if b == "dollar":
    print(a/428.38,"USD")
elif b == "euro":
    print(a/522.38, "EUR")
elif b == "rouble":
    print(a/5.82,"RUR")

#6
n = int(input())
for i in range(n+1):
    print(i*i,end=" ")

#7
n = input()
sum = 0
for i in range(len(n)):
    sum += int(n[i])
print(sum)

#8
n = input()
sum = 0
for i in range(len(n)):
    sum += int(n[i])
print(sum/len(n))

#9
a = input()
if a == a[::-1]:
    print("You catch a palindrome")
else:
    print("Not palindrome")