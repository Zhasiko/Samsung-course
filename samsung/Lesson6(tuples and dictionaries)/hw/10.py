s1 = {'f', 't', 'c', 'a', 'x', 'd', 'e', 'b', 'y', 'z'}
s2 = {'b', 'c', 'e', 'z', 'x', 'a', 'y'}
if s1.issubset(s2):
    print("Subset")
elif s1.issuperset(s2):
    print("Superset")