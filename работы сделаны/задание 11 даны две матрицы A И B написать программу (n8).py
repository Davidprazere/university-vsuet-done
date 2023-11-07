"""""" даны две матрицы
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def print_twin_primes(n):
    for i in range(n, 2*n-2):
        if is_prime(i) and is_prime(i+2):
            print(i, i+2)
