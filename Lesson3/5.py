def naim(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c

x = int(input())
y = int(input())
z = int(input())

print(naim(x,y,z))
