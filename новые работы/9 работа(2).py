def filter_columns(matrix, max_absolute_value=10):
    filtered_columns = []
    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]
        if all(abs(element) <= max_absolute_value for element in column):
            filtered_columns.append(column)
    return filtered_columns

def find_min_product_column(filtered_columns):
    min_product = float('inf')
    min_product_column = None

    for column in filtered_columns:
        product = 1
        for element in column:
            product *= element
        if product < min_product:
            min_product = product
            min_product_column = column

    return min_product_column

def swap_with_neighbor(matrix, column_index):
    for i in range(len(matrix)):
        matrix[i][column_index], matrix[i][column_index + 1] = matrix[i][column_index + 1], matrix[i][column_index]

# Пример использования
matrix = [
    [5, 3, 8, 7],
    [-2, -1, 10, 5],
    [15, 2, 6, -3]
]

filtered_columns = filter_columns(matrix)
min_product_column = find_min_product_column(filtered_columns)

if min_product_column is not None:
    min_product_column_index = matrix[0].index(min_product_column[0])
    swap_with_neighbor(matrix, min_product_column_index)
    print("Матрица после замены:")
    for row in matrix:
        print(row)
else:
    print("Нет подходящих столбцов.")