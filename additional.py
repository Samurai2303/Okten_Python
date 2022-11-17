# створити декоратор який буде рахувати кількість запущених функцій продекорованих цим декоратором

from typing import Callable, Any


def counter() -> Callable[[], int]:
    count = 0

    def get_count() -> int:
        nonlocal count
        count += 1
        return count

    return get_count


get_count = counter()


def decor(func: Callable[[Any], Any]) -> Callable[[Any], None]:
    def inner(*args, **kwargs) -> None:
        count = get_count()
        func(*args, **kwargs)
        print(f'count: {count}')

    return inner


@decor
def func_1() -> None:
    print('func_1')


@decor
def func_2() -> None:
    print('func_2')


func_1()
func_2()
func_2()
func_1()


# вивести послідовність Фібоначі, кількість вказана в знінній,
# наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
# (число з послідовності - це сума попередніх двох чисел)

def fibonachi(a: int) -> None:
    l = []
    for i in range(a):
        if i > 1:
            l.append(l[i - 2] + l[i - 1])
        elif i <= 1:
            l.append(1)
    print(l)


fibonachi(10)


# порахувати кількість парних і непарних цифр числа,
# наприклад: х = 225688 -> п = 5, н = 1;
# х = 33294 -> п = 2, н = 3

def odd_even(number: int) -> list[int]:
    l = [i for i in str(number)]
    odd = 0
    even = 0
    for i in l:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return [odd, even]


print(odd_even(127584373))

# прога, що виводить кількість кожного символа з введеної строки, наприклад:
st = 'as 23 fdfdg544'  # введена строка


# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2

def amount_of_symbols(string: str) -> None:
    l = [i for i in string]
    l.sort()
    for i in range(len(l)):
        if len(l):
            count = l.count(l[0])
            print(f'\'{l[0]}\': {count}')
            for j in range(count):
                l.pop(0)


amount_of_symbols(st)


# # генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# # задача сделать c него лист листов такого плана:
# #
# # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# # [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# # [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# # [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]

def list_of_lists(length: int)->None:
    l = []
    result = []
    for i in range(length * 2):
        if i % 2 == 1:
            l.append(i)
    for i in range(len(l)):
        if len(l):
            list1 = []
            for j in range(i + 1):
                if len(l):
                    list1.append(l[0])
                    l.pop(0)
            result.append(list1)
    print(result)


list_of_lists(12)


# найти со списка только уникальные числа
# пример [1,2,3,4,2,5,1] => [ 3, 4, 5 ]

def unique_numbers(list: list[int])->None:
    list.sort()
    l = []
    for i in range(len(list)):
        if len(list):
            count = list.count(list[0])
            if count == 1:
                l.append(list[0])
            for j in range(count):
                list.pop(0)
    print(l)


unique_numbers([1, 2, 3, 4, 2, 5, 1])