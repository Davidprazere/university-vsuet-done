# Инициализация переменных
max_number = second_max_number = float('-inf')

# Ввод последовательности чисел
while True:
    num = int(input("Введите число (0 для завершения): "))
    
    if num == 0:
        break
    
    # Обновление наибольшего и второго по величине чисел
    if num > max_number:
        second_max_number = max_number
        max_number = num
    elif num > second_max_number:
        second_max_number = num

# Вывод результата
if second_max_number == float('-inf'):
    print("В последовательности не хватает чисел для определения второго по величине элемента.")
else:
    print("Второй по величине элемент в последовательности:", second_max_number)