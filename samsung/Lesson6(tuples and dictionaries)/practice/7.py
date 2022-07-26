a_dict = {'палатка' : 5,
"спальный мешок" : 3,
'удочка' : 2,
'термос': 2,
'салфетки' : 1,
'жвачка' : 1}

n = int(input())
cost = 0


for i in a_dict:
    if n >= (cost + a_dict[i]):
        cost += a_dict[i]
        print(i, cost)