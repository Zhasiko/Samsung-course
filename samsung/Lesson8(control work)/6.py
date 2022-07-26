A = [random.randrange(0, 3) for i in range(10)]
B = []
C = []
print(A)

x = A[0]
B.append(x)
C.append(1)
k = 0
for i in range(1, 10) :
    if x == A[i]:
        C[k] += 1
    else:
        x = A[i]
        B.append(x)
        C.append(1)
        k += 1

print("Array B:")
print(B)
print("Array C:")
print(C)