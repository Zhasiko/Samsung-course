n = int(input())
new_lst = [[i for i in range(n)] for _ in range(2)]
print(new_lst)
print('Yes' if new_lst[0] == new_lst[1] else 'No')