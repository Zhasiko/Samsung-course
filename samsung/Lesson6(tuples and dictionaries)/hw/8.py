a_dict = {'alphas' : 0,
'digits' : 0}
s = input()
for i in s:
    if ord(i) in range(65,123):
        a_dict['alphas'] += 1
    elif ord(i) in range(48,58):
        a_dict['digits'] += 1
print(a_dict)