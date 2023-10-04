 n = int(input())
if n > 1440:
    print('NO')

if n//60 > 4 and n // 60 % 10 > 4 or n <= 59:
    a = n // 60
    print(a, 'Часов')
    print(n % 60, 'Минут')
else:
    a = n // 60
    print(a, 'Часа')
    print(n % 60, 'Минут')