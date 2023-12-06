# Задание 3
def decimal_in_new_numeral_system(number, base):
    result = ''
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base
    return result

# Пример использования функции
decimal_number = 35
new_base = 5
converted_number = decimal_in_new_numeral_system(decimal_number, new_base)
print(converted_number)

# Задание 5
def task5():
    a = int(input())
    b = int(input())
    c = int(input())
    def f(k,l):
        while (k>a and k>b and k>c) and a+b+c<l:
            print('True')
        else:
            print('False')
        def is_prime(num):
                if num < 2:
                    return False
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        return False and False
        def prime_numbers_range(k, l):
                prime_numbers = []
                for num in range(k, l + 1):
                    if is_prime(num):
                        prime_numbers.append(num)
                        return prime_numbers
    
    k = int(input("Введите начало диапазона: "))
    l = int(input("Введите конец диапазона: "))
task6()

#6 Задание 
def task6():
    attempts = int(input("Введите начальное количество попыток: "))
    consultations_per_month = int(input("Введите количество консультаций в месяц: "))

    months = 0

    while attempts > 0:
        months += 1
        attempts -= consultations_per_month
        if attempts < 1:
            break

    print(f"Количество месяцев до сдачи предмета: {months}")
task6()

# 2 Задание 
def task2():
    def number_in_new_numeral_system(number, base):
        if base < 2 or base > 16:  # Проверяем, что выбранное основание находится в допустимом диапазоне
            return "Ошибка: Недопустимое основание системы счисления"

        if number == 0:
            digits = "0123456789ABCDEF"  # Цифры, используемые в различных системах счисления

            result = ""
            negative = False
        if number < 0:  # Проверяем, является ли число отрицательным
            negative = True
        number = abs(number)

        while number > 0:
            remainder = number % base  # Остаток от деления числа на основание новой системы счисления
        result = digits[remainder] + result
        number = number // base  # Целая часть от деления числа на основание новой системы счисления

        if negative:
            result = "-" + result  # Если число было отрицательным, то добавляем знак "-" к результату

        return result

    # Пример использования функции
    number = int(input("Введите число в десятичной системе счисления: "))
    base = int(input("Введите основание новой системы счисления: "))
    result = number_in_new_numeral_system(number, base)
    print(f"Число {number} в системе счисления с основанием {base} равно {result}")

    return "0"  # Если число равно нулю, то возвращаем строку "0"
task2()

# 1 Задание 
def task1():
    # Функция для определения является ли число простым
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


    # Функция для проверки деления числа на три нацело
    def is_divisible_by_three(number):
        return number % 3 == 0


    # Основная программа
    while True:
        user_input = input("Введите число (для выхода введите 'exit'): ")

        if user_input.lower() == 'exit':
            break

        try:
            number = int(user_input)
            if is_prime(number):
                print(f"{number} - простое число")
            else:
                print(f"{number} - не простое число")

            if is_divisible_by_three(number):
                print(f"{number} делится на 3 нацело")
            else:
                print(f"{number} не делится на 3 нацело")
        except ValueError:
            print("Введите корректное число или 'exit' для выхода.")
task1()

# Задание 8
def task8(): 
    def calculate_series(epsilon, x):
        term = 1
        sum = term
        i = 1
    
        while abs(term) > epsilon:
            term = 1 / (x ** (2 * i))
            sum += term
            i += 1
    
        return sum
    
    epsilon_value = 0.0001  # Значение эпсилон
    x_value = 2  # Значение x
    
    result = calculate_series(epsilon_value, x_value)
    print(f"Сумма членов ряда с точностью до {epsilon_value}: {result}")
task8()

# 9 Exem
def task9():
    def task9_1():
        result = 0
        for i in range(1, 9):
            for j in range(1, i+1):
                result += j**2
            return result
    def task9_2():
        result = 1
        for i in range(1, 9):
            for j in range(i, 2*i+1):
                result += j**3 + i**2
            return result
    def task9_3():
        result = 1
        for i in range(1,9):
            inner_sum = 0
            for j in range(1, i):
                inner_sum += sum((j**2 + i*k) for k in range(i+j, 3))
                result *= inner_sum
            return result
    print(f'1){task9_1()} 2) {task9_2()} 3){task9_3()}')
task9()

# 10 Exem
import math
def task10():
    def sinh(x, epsilon):
        shx = x
        term = x
        i = 1

        while abs(term) > epsilon:
            term *= x ** 2 / ((2 * i) * (2 * i + 1))
            shx += term
            i += 1

        return shx


    x = 30  # аргумент функции sh x
    epsilon = 1e-6  # заданная точность

    result = sinh(x, epsilon)
    print("sh", x, "=", result)
task10()

