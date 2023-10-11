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
            return False
    return True

def prime_numbers_range(k, l):
    prime_numbers = []
    for num in range(k, l + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

k = int(input("Введите начало диапазона: "))
l = int(input("Введите конец диапазона: "))
