def quantity_dolek(a, b, c):
    if a*b % c == 0:
        return 'Да'
    else:
        return 'Нет'

n = int(input())
m = int(input())
k = int(input())

print(quantity_dolek(n,m,k))