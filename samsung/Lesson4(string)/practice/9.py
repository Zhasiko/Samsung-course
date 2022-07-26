s,l = input(),input()
for c in ['a', 'e', 'i', 'o', 'u']:
    if c in s:
       a = s.replace(c,l)
       s = a
print(s)