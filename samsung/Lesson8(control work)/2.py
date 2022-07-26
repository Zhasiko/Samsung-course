dict= {} 
for i in range(int(input())): 
    a, b, c = input().split() 
    dict[a] = dict.get(a, {}) 
    dict[a][b] = dict.get(a, {}).get(b, 0) + int(c) 
for i in sorted(dict): 
    print(f'{i}:', end='\n') 
    for k in sorted(dict[i]): 
        print(f'{k} {dict[i][k]}', end='\n')