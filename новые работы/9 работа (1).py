def find_min_element_row_sum(matrix):
    # Находим индексы минимального элемента
    min_element_value = float('inf')  # Инициализируем переменную значением бесконечности
    min_row_index = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_element_value:
                min_element_value = matrix[i][j]
                min_row_index = i

    # Суммируем элементы в найденной строке
    row_sum = sum(matrix[min_row_index])

    return row_sum

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = find_min_element_row_sum(matrix)
print("Сумма элементов строки с минимальным значением:", result)