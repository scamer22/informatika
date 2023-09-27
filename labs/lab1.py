def task1():
    from math import *

    x = int(input())
    y = int(input())
    z = int(input())

    l = log10(1 + x ** 2) - abs(y ** (1 / 3))
    r = x ** (1 / 3) + y ** (1 / 4)
    a = l / r
    b = z ** (1 / 2) + y ** 2 + log(x)

    print(a, b)

task1()

def task2():
 from math import *

 a = 1
 b = 3
 c = -4

 def f(x):
     return x ** b + ((b * x) ** (1 / 2)) / c * x + a

 print(f(x))
task2()

def task3():
 from math import *

 def f(x):
     return 3 ** (-2 * x) - ((cos(x) + sin(3 * x)) ** (1 / 3))

 print(f(x))
task3()

def task4():
 from math import *

 r = int(input())
 h = int(input())

 v = 1 / 3 * pi * (r ** 2) * h
 l = r ** 2 + h ** 2

 print(l)
task4()

def task5():
 v1 = float(input())
 v2 = float(input())
 h = float(input())

 time = h / (v1 - v2)
 distance = v1 * time

 print(time)
 print(distance)

task5()

def task6():
 import math

 def f(l, a):
     h = math.sqrt(l ** 2 - a ** 2)
     return h

 l = float(input())
 a = float(input())
 h = f(l, a)

 print(h)

task6()

def task7():
 import math

 A = float(input())
 B = float(input())
 C = float(input())

 D = B ** 2 - 4 * A * C

 if D >= 0:
     x1 = (-B + math.sqrt(D)) / (2 * A)
     x2 = (-B - math.sqrt(D)) / (2 * A)

     print(x1)
     print(x2)
 else:
     print('aye')

task7()

def task8():
 def f(v, a):
     t = (2 * v) / a
     s = (a * (t ** 2)) / 2
     return s

 v = float(input())
 a = float(input())
 l = f(v, a)

 print(l)

task8()

def task9():
    
    def f(value, total):
        percentage = (value / total) * 100
        if percentage > 5:
            return percentage
        else:
            return 5
    
    print(f())

task9()



