# Задание 4
def lace_length(a, b, c, d):
    sum_a = (a * (d - 1)) * 2
    sum_b = (b * (d - 1)) * 28
    return sum_a + sum_b + c


znach_a = int(input())
znach_b = int(input())
l = int(input())
N = int(input())

print(lace_length(znach_a, znach_b, l, N))

