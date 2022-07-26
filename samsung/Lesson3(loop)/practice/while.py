import random

secretVal = random.randint(1,10)

count = 1
while count <= 8:
    myVal = int(input(f"Your int: , count {count} "))
    if myVal > secretVal:
        print("bigger")
    elif myVal < secretVal:
        print('less')
    else:
        print(f"found  {count}")
        break
    count+=1