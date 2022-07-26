d = {}
n = int(input())
for i in range(n):
    s = input().split()
    d.update({s[0]:s})
m = int(input())
for i in range(m):
    l = input().split()
    if l[0] == 'read' and "R" in d.get(l[1]):
        print("OK")
        continue
    if l[0] == 'write' and "W" in d.get(l[1]):
        print("OK")
        continue
    if l[0] == 'execute' and "X" in d.get(l[1]):
        print("OK")
        continue
    else:
        print("Access denied")