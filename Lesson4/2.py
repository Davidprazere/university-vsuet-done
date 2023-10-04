A = int(input())
B = int(input())

if A < B:
    while A != B+1:
        print(A)
        A += 1
else:
    while A != B-1:
        print(A)
        A -= 1
