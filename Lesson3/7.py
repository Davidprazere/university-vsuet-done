def visocos(x):
    if x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 400 == 0:
        return True
    else:
        return False

Year = int(input())

if visocos(Year):
    print('Да')
else:
    print('Нет')