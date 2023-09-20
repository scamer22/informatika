#Задание 1
#from math import *

x = int(input())
y = int(input())
z = int(input())

l = log10(1 + x**2) - abs(y**(1/3))
r = x ** (1/3) + y**(1/4)
a = l / r
b = z**(1/2) + y**2 + log(x)

print(a, b)

#задание 2
#from math import *

a = 1
b = 3
c = -4

def f(x):
    return x**b + ((b*x)**(1/2)) / c*x+a

print(f(x))

#Задание 3
from math import *

def f(x):
    return 3**(-2*x) - ((cos(x) + sin(3*x))**(1/3))
print(f(x))

#Задание 4
