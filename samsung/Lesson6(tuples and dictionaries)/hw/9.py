s1 = {'a', 'b', 'c', 'd', 'e', 'f', 't'}
s2 = {'b', 'c', 'e', 'z', 'x', 'a', 'y'}

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference a - b:", s1.difference(s2))
print("Difference b - a", s2.difference(s1))