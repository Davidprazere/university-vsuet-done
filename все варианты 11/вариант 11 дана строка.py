def process_string(input_str):
    max_n_sequence = max((list(g) for k, g in itertools.groupby(input_str) if k == 'н'), key=len, default=[])
    result_str = input_str.replace('!', '.') if max_n_sequence else input_str
    return result_str

# Пример использования:
input_str = "нннабб!н!нннн!ввв"
result = process_string(input_str)
print(result)