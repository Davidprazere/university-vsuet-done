A = int(input())
B = int(input())

if A > B:
    while A != B-1:
        x = A
        if x % 2 != 0:
            print(A)
            A -= 1
        else:
            A -= 1