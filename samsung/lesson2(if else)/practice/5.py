n = int(input())
if 0 < n < 10:
    print('Число однозначное положительное')
elif 9 < n < 100:
    print('Число двухзначное положительное')
elif 99 < n < 1000:
    print('Число трехзначное положительное')
elif -10 < n < 0:
    print('Число однозначное отрицательное')
elif -100 < n < -9:
    print('Число двухзначное отрицательное')
elif -1000 < n < -99:
    print('Число трехзначное отрицательное')