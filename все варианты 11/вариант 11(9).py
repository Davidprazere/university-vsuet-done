def find_min_row_sum(matrix):
    min_row_index = 0
    min_value = float('inf')

    
    for i, row in enumerate(matrix):
        current_min = min(row)
        if current_min < min_value:
            min_value = current_min
            min_row_index = i


    min_row_sum = sum(matrix[min_row_index])

    return min_row_sum


matrix_data = [
    [1, 2, 3],
    [4, 1, 6],
    [7, 8, 1]
]

result = find_min_row_sum(matrix_data)
print(f"Сумма элементов строки с минимальным значением: {result}")