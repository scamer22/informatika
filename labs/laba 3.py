#1 ex
def print_char_list(array):
    for char in array:
        print(char)


def proverka1(array, symbol):
    if symbol in array:
        print(f"Символ '{symbol}' входит в последовательность.")
    else:
        print(f"Символ '{symbol}' не входит в последовательность.")


def proverka2(array, first_symbol, second_symbol):
    count = 0
    for i in range(len(array) - 1):
        if array[i] == first_symbol and array[i + 1] == second_symbol:
            count += 1
    print(f"Количество пар соседних символов '{first_symbol}{second_symbol}': {count}")


def proverka3(array):
    count = 0
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            count += 1
    print(f"Количество пар соседних одинаковых символов: {count}")


def proverka4(array):
    for i in range(1, len(array) - 1):
        if array[i] == array[i + 1] and array[i - 1] == array[i]:
            print("Существуют такие i и j, что 1 < i < j < n и символы совпадают.")
            return
    print("Таких i и j не существует.")


def proverka5(array):
    count = 0
    for char in array:
        if char == ' ':
            count += 1
    print(f"Количество пробелов в последовательности: {count}")


def task1():
    n = int(input("Введите количество символов: "))
    array = []
    print("Введите последовательность символов:")
    for i in range(n):
        symbol = input(f"Символ {i + 1}: ")
        array.append(symbol)

    print_char_list(array)
    print()

    symbol1 = input("Введите символ для проверки (proverka1): ")
    proverka1(array, symbol1)

    symbol2_1 = input("Введите первый символ для проверки (proverka2): ")
    symbol2_2 = input("Введите второй символ для проверки (proverka2): ")
    proverka2(array, symbol2_1, symbol2_2)

    proverka3(array)

    proverka4(array)

    proverka5(array)


task1()

#3 ex
def task3():
    for i in range(5):
        print("Введите текст:")
        text = input("Введите текст: ")
        with open("file.txt", "a") as file:
            file.write(text + "\n")

# Call the function to run it
task3()

