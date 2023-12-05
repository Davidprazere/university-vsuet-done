def find_max(matrix):
    max_element = matrix[0][0]
    max_coords = (0, 0)
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem > max_element:
                max_element = elem
                max_coords = (i, j)
    return max_coords

def swap_max_elements(matrix_a, matrix_b):
    max_a = find_max(matrix_a)
    max_b = find_max(matrix_b)

    matrix_a[max_a[0]][max_a[1]], matrix_b[max_b[0]][max_b[1]] = matrix_b[max_b[0]][max_b[1]], matrix_a[max_a[0]][max_a[1]]

# Пример использования:
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

swap_max_elements(matrix_A, matrix_B)
print(matrix_A)
print(matrix_B)