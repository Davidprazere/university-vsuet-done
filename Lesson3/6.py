def chetnechet(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return True
    elif a % 2 != 0 and b % 2 != 0:
        return True
    else:
        return False


x = int(input()) # Если цифра нечетная, то клетка черная и наоборот
y = int(input())

if chetnechet(x, y):0
    print('Да')
else:
    print('Нет')