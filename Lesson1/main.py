print('Курс Основы программирования начался')
print(16823 * 12302 % 3092)

name = str(input('Введите ваше имя '))
if name == 'Иван':
    print('Увы')
    quit()

age = int(input('Введите ваш возраст '))
if 0 < age < 75 and age >= 16:
    print('Поздравляем вы поступили в ВГУИТ')
elif 0 < age < 16:
    print('Сначала нужно окончить школу!')
    print('Вам осталось учиться', 16 - age)
elif age == 0 or age < 0:
    print('Не балуйся')
elif age > 74:
    print('Вам пора на пенсию')

