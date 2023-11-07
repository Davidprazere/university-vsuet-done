'''
Определите среднее значение всех элементов последовательности,
завершающейся числом 0.
'''

total = 0
iteR = 0
inp = int(input())

while inp != 0:
    total += inp        
    iteR +=1            
    inp = int(input())  
    
print(total / iteR)     