import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return(False)
        else:
            return (True)
def TWINS(n):
    if prime(n) and prime(n-2) or prime(n+2):
        return prime(n)
n = int(input())
print(*filter(TWINS, [x for x in range(n, 2*n+1)]))
