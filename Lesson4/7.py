def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

N = int(input())
S = [int(x) for x in range(1, N+1)]
summa = 0

for j in range(len(S)):
    summa += factorial(S[j])

print(summa)