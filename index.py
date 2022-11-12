# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
st = 'as 23 fdfdg544'  # введена строка
# 2,3,5,4,4        #вивело в консолі.

# print(', '.join([i for i in st if i.isnumeric()]))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
st1 = 'as 23 fdfdg544 34'  # введена строка
#   23, 544, 34              #вивело в консолі

# print(', '.join(''.join([i if i.isnumeric() else ' ' for i in st1]).split()))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
greeting = 'Hello, world'


# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# print([i for i in greeting.upper()])

#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i ** 2 for i in range(50) if i % 2 == 0])


#
# function
#
# - створити функцію яка виводить ліст

def print_list(list):
    print(list)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_number(a, b, c):
    l = [a, b, c]
    print(max(l))
    return max(l)


# max_number(12, 1, -4)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def max_min_number(*args):
    print(max(args))
    return min(args)


# max_min_number(1,2,4,-4,6,56,5,93)

# - створити функцію яка повертає найбільше число з ліста

def max_from_list(list):
    return max(list)


# max_from_list([12,3,45,8,46,6,5])

# - створити функцію яка повертає найменьше число з ліста

def min_from_list(list):
    return min(list)


# min_from_list([12, 3, 45, 8, 46, 6, 5])

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)
    return sum


# sum([3,4,33,-23,-9,-23,121])

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def average(list):
    average = 0
    for i in list:
        average += i / len(list)
    print(average)
    return average


# average([2,3,34,5,-57,7,9,8])

# ################################################################################################
# 1)Дан list:
list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число

# print(min(list1))

#   - видалити усі дублікати

# print(list(set(list1)))

#   - замінити кожне 4-те значення на 'X'

def every_4_to_x(list):
    list = ['X' if i % 4 == 0 else v for i, v in enumerate(list)]
    print(list)
    return list


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square(a):
    star = '*'
    space = ' '
    b = a - 2
    for i in range(a):
        if i == 0 or i == a - 1:
            print(star * a)
        else:
            print(f'{star}{space * b}{star}')


# 3) вывести табличку множення за допомогою цикла while

def multiplication_table():
    i = 1
    while i < 10:
        j = 0
        str = ''
        while j < 10:
            j += 1
            num = i * j
            if num < 10:
                str = f'{str}   {num}'
            else:
                str = f'{str}  {num}'
        print(str)
        i += 1


# 4) переробити це завдання під меню

# x = input('enter number')

def x_func():
    print('1 - multiplication table')
    print('2 - square')
    print('3 - every 4 to X')
    print('4 - average')
    print('5 - sum')
    print('6 - exit')
    x = input('enter number')
    return x


def menu(x):
    if x == 1:
        multiplication_table()
        x1 = x_func()
        menu(int(x1))
    elif x == 2:
        square(10)
        x1 = x_func()
        menu(int(x1))
    elif x == 3:
        every_4_to_x(list1)
        x1 = x_func()
        menu(int(x1))
    elif x == 4:
        average([1, 23, 3, -54, 6, -6, 54])
        x1 = x_func()
        menu(int(x1))
    elif x == 5:
        sum(list1)
        x1 = x_func()
        menu(int(x1))
    elif x == 6:
        print('finish')
    else:
        print('error')

x1 = x_func()
menu(int(x1))