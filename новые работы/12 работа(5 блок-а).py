def print_digits_reverse(n):
    # Базовый случай: если число n однозначное
    if n < 10:
        print(n)
    else:
        # Вывести последнюю цифру
        print(n % 10)
        # Рекурсивно вызвать функцию для оставшейся части числа
        print_digits_reverse(n // 10)

# Пример использования
number = 12345
print("Цифры числа", number, "в обратном порядке:")
print_digits_reverse(number)