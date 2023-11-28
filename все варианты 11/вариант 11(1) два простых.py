def twin_primes_range(n):
    twin_primes = []
    for num in range(n, 2 * n - 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            if all((num + 2) % i != 0 for i in range(2, int((num + 2)**0.5) + 1)):
                twin_primes.append((num, num + 2))
    return twin_primes

# Пример использования:
n_value = 20
result = twin_primes_range(n_value)
print(result)