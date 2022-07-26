def digitize(n):
    return map(int, str(n)[::-1])

digitize(12345)