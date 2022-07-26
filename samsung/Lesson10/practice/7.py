def iso(s):
    return True if len(set(s.upper())) == len(s) else False
print(iso(input()))