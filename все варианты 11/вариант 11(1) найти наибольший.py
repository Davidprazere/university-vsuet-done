def max_even_divisible_by_2(lst):
    evens = [x for x in lst if x % 2 == 0]
    if not evens:
        print("Нет четных чисел, делящихся на 2 без остатка.")
        return None
    return max(evens)

# Пример использования:
numbers = [1, 3, 6, 8, 12, 7]
result = max_even_divisible_by_2(numbers)
print(result)