#1
def hello():
    print( "Hello!")
    
hello()

#2
def hello(name):
    print('Hello', name)
    
hello(input())

#3
def hello(name = 'Anonym'):
    print("Hello", name)

hello()

#4
def maximum(n,m):
    return max(n,m)
print(maximum(int(input()),int(input())))

#5
def minimum(a):
    return min(a)
print(minimum([int(i) for i in input().split()]))

#6
def extr(a):
    return min(a),max(a)
print(extr([int(i) for i in input().split()]))

#7
def aver(*a):
    return sum(a)/len(a)
print(aver(1,2,3,4))

#8

def dictn(**a):
    return a

print(dictn(name = "PY", version = 3.8))

#9
res = 1
def factorial(n):
    global res
    while n > 1:
        res *= n
        return factorial(n-1)
    else:
        return res
print(factorial(int(input())))