def swap_columns(matrix):
    valid_columns = [col for col in zip(*matrix) if all(abs(element) <= 10 for element in col)]
    min_product_column = min(valid_columns, key=lambda col: functools.reduce(operator.mul, col, 1))
    
    if min_product_column:
        min_index = matrix[0].index(min_product_column[0])
        adjacent_index = min_index - 1 if min_index > 0 else min_index + 1
        for row in matrix:
            row[min_index], row[adjacent_index] = row[adjacent_index], row[min_index]

# Пример использования:
matrix = [
    [1, 2, 10],
    [4, 5, -6],
    [-7, 8, 9]
]
swap_columns(matrix)
print(matrix)