# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

# 2) протипізувати перше завдання
from typing import Callable, Any


def todo_list() -> list[Callable[[str], None] | Callable[[], list[str]]]:
    l: list[str] = []

    def add_todo(todo: str) -> None:
        l.append(todo)

    def get_todos() -> list[str]:
        return l

    return [add_todo, get_todos]


add_todo, get_todos = todo_list()

add_todo('todo 1')
add_todo('todo 2')
print(get_todos())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(number: int) -> str:
    num_list: list[str] = [i for i in str(number)]
    num_list.reverse()
    string = ''
    for i in range(len(num_list)):
        if int(num_list[i]) > 0:
            string = f'{num_list[i]}{"0" * i} + {string}'
    string = string.rstrip('+ ')
    return string


string = expanded_form(10457040504)
print(string)


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
# продекорована цим декоратором, та буде виводити це значення після виконання функцій


def decor(func: Callable[[Any], Any]) -> Callable[[Any], None]:
    count = 0

    def inner(*args, **kwargs) -> None:
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'count:{count}')

    return inner


@decor
def test_function(a) -> None:
    print(a)

test_function(8765)
test_function(342)
test_function(1345)
test_function(452)
