def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(float, line.split()))  # Предполагаем, что числа в матрице разделены пробелами
            matrix.append(row)
    return matrix

def write_matrix_to_file(file_name, matrix):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n') 

# Замените 'your_file_name' на реальное имя файла
input_file_name = 'ФИО_группа_vod.txt'
output_file_name = 'ФИО_группа_vivod.txt'

# Чтение матрицы из файла
matrix = read_matrix_from_file(input_file_name)

# Выполнение каких-то операций с матрицей (например, транспонирование)
# В данном примере мы транспонируем матрицу (меняем строки и столбцы местами)
transposed_matrix = [list(row) for row in zip(*matrix)]

# Запись результата в файл
write_matrix_to_file(output_file_name, transposed_matrix)
