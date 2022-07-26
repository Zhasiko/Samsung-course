def massive_func(massive):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for word in massive:
        count = 0
        for c in word:
            if c in vowels:
                count += 1
        if count >= 4:
            res.append(word)
    return res