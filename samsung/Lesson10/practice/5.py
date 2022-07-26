def flow(f1,f2):
    return False if f1%2 == f2%2 else True

print(flow(int(input()), int(input())))