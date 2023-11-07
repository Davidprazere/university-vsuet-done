x = int(input())
y = int(input())
i = 1               

while x < y:
    x += x * 0.1    
    i += 1          
    
print(i)