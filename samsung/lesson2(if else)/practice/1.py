sum = int(input('Insert amount in KZT: '))
currency = int(input('Choose currency: [1] USD [2] EUR [3] GBP 2: '))

if currency == 1:
    curName = 'USD'
    value = sum / 320
elif currency == 2:
    curName = 'EUR'
    value = sum / 360
elif currency == 3:
    curName = 'GBP'
    value = sum / 420

print(str(value), curName)
