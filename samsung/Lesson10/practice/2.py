def summ(n):
    if n > 0:
        return n % 10 + summ(n // 10)
    else:
        return 0

print(summ(int(input())))