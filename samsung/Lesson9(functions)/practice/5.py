def func(a,b,c):
    if int(str(a)[-1]) * int(str(b)[-1]) == int(str(c)[-1]):
        print(True)
    else:
        print(False)
     
a = int(input())
b = int(input())  
c = int(input())  
func(a,b,c)