def even_numbers_lt_10(arr):
    result = [x for x in arr if x % 2 == 0 and x < 10]
    if not result:
        print("Нет четных чисел, меньших 10.")
    else:
        result.sort()
        print(result)

# Пример использования:
array = [1, 5, 8, 3, 12, 6]
even_numbers_lt_10(array)