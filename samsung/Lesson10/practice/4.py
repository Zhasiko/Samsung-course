def fucn(s):
    res = ''
    for i in range(len(s)-1):
        if s[i] == "-":
            res += s[i+1].upper()
        elif s[i] == "_":
            res += s[i+1]
        elif s[i] != "-" or s[i] != "_":
            res += s[i]
    return res

print(fucn(input()))