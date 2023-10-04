def fibonaci(n):
    if n in (1, 2):
        return 1
    return fibonaci(n - 1) + fibonaci(n - 2)

S = 0
N = int(input())
for x in range(1, N+1):
    S += fibonaci(x)

print(S)
