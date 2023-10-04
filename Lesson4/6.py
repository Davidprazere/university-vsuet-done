N = int(input())
S = [int(x) for x in range(1, N+1)]
factor_N = 1
for y in range(len(S)):
        factor_N = factor_N * S[y]
print(factor_N)
