import math

x = 0.1722
y = 6.33
z = 3.25*10**(-4)

a = 5 * math.atan(x)
b = (x + 3*abs(x-y) + x**2)/(abs(x-y)*z + x**2)

s = a - (1/4*math.acos(x))*b
print(s)
