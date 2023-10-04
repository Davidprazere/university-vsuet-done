def matching_numbers(x, y, z):
    if x == y == z:
        return 3
    if x == y or x == z or y == z:
        return 2
    else:
        return 0

number1 = int(input())
number2 = int(input())
number3 = int(input())

print(matching_numbers(number1, number2, number3))

