def store(*a):
    q = 0
    cost = 0
    for i in a:
        q += i['quantity']
    cost = q * a[i]['price']
    return cost

a = [[dict(j) for j in input().split()] for i in input().split()]  
store(a)