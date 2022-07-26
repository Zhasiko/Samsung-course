sum = 0
count = 0  # счетчик
while True:
    n = int(input("n: "))
    if n == 0:
        break
    count += 1
    sum += n

print(sum / count)
print(count)