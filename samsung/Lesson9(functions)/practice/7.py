def happy(a):
    while True:
        n = []
        for i in range(len(a)):
            n.append(i)
        s = ""
        if set(n) == n:
            return 'ok'
        else:
            for i in range(len(n)):
                s += str(n[i])
            n = int(s) + 1

a = input()
happy(a)