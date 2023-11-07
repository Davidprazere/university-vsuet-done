n = int(input())
x = 1

while 2 ** x <= n:  
    x += 1          
x -= 1             

print(x, 2 ** x)