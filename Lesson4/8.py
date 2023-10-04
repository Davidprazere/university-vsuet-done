N = int(input())
step = ''

if N <= 9:
    for i in range(1, N+1):
        step += str(i)
        print(step)
