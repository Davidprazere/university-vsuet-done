def min_row_sum(matrix):
    min_value_row = min(matrix, key=lambda row: sum(row))
    return sum(min_value_row)

# Пример использования:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = min_row_sum(matrix)
print(result)