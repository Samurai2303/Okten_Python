# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
try:
    with open('emails.txt') as file, open('emails1.txt', 'w') as new_file:
        string_list = file.readlines()
        new_str = ''
        for i in range(len(string_list)):
            email_name = string_list[i].split('\t\t\t')[1].split('@')[0]
            new_str = f'{new_str}{email_name}@gmail.com\n'
        new_file.write(new_str)
except Exception as err:
    print(err)

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

file_name = 'purchase.list.txt'
ipt = '0'
id = 1
try:
    with open(file_name) as file:
        lines_list = file.readlines()
        if len(lines_list):
            id = int(lines_list[len(lines_list) - 1].split('\t')[0].split(':')[1]) + 1
except Exception:
    pass


def menu_header():
    global ipt
    print('1 - Show all purchases')
    print('2 - Add purchase')
    print('3 - Search by field')
    print('4 - Show the most expensive')
    print('5 - Delete by id')
    print('0 - exit')
    ipt = input('Enter number:')


def purchase_book():
    global ipt

    menu_header()

    match ipt:
        case '1':
            try:
                with open(file_name) as file:
                    print(file.read())
            except Exception as err:
                print(f'case1 - {err}')
        case '2':
            try:
                with open(file_name, 'a') as file:
                    global id
                    can_continue = False
                    while not can_continue:
                        name = input('Enter name of purchase:')
                        price = input('Enter price of purchase:')
                        if name != '' and price.isnumeric():
                            can_continue = True
                        else:
                            can_continue = False
                            print('Name or price is incorrect! Try again')
                    file.write(f'ID:{id}\tName:{name}\tPrice:{price}\n')
                    id += 1
            except Exception as err:
                print(f'case2 - {err}')
        case '3':
            try:
                with open(file_name, 'r') as file:
                    can_continue = False
                    while not can_continue:
                        search_str = input('Enter id, name or price of the purchase:')
                        if search_str != '':
                            can_continue = True
                        else:
                            print('You must enter smth in this search field')
                            can_continue = False
                    lines_list = file.readlines()
                    purchases_list = []
                    for line in lines_list:
                        line_parts = line.split('\t')
                        for part in line_parts:
                            listV = part.split(':')
                            if listV[1].find(search_str) >= 0:
                                can_add = True
                                for item in purchases_list:
                                    if line == item:
                                        can_add = False
                                if can_add:
                                    purchases_list.append(line)
                    if len(purchases_list):
                        for purchase in purchases_list:
                            print(purchase)
                    else:
                        print('Have no coincidence(')
            except Exception as err:
                print(f'case3 - {err}')
        case '4':
            try:
                with open(file_name) as file:
                    lines_list = file.readlines()
                    purchase = None
                    most_expensive = 0
                    for line in lines_list:
                        line_parts = line.split('\t')
                        splited_price = line_parts[2].split(':')
                        if int(splited_price[1]) > most_expensive:
                            most_expensive = int(splited_price[1])
                            purchase = line
                    print(purchase)
            except Exception as err:
                print(f'case4 - {err}')
        case '5':
            new_list = []
            try:
                with open(file_name) as file:
                    can_continue = False
                    while not can_continue:
                        del_id = input('Enter purchase id:')
                        if del_id.isnumeric():
                            can_continue = True
                            del_id = int(del_id)
                        else:
                            print('delete ID must be a number')
                            can_continue = False
                    del_line = None
                    lines_list = file.readlines()
                    for line in lines_list:
                        line_parts = line.split('\t')
                        if int(line_parts[0].split(':')[1]) == del_id:
                            del_line = line
                    if del_line:
                        lines_list.pop(lines_list.index(del_line))
                        new_list = lines_list
                    else:
                        print('Have no item with this id')
            except Exception as err:
                print(f'case5R - {err}')
            try:
                with open(file_name, 'w') as file:
                    file.write(''.join(new_list))
                    print('Done!')
            except Exception as err:
                print(f'case5W - {err}')
        case '0':
            print('Finish!')
        case _:
            print('Wrong number! Try again')

    if ipt.isnumeric():
        if int(ipt) > 0:
            purchase_book()
    else:
        purchase_book()


purchase_book()

# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# в результат має записатись тільки 5 id
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]
def gen(team):
    for i in team:
        yield i

gen1 = gen(data[0])
gen2 = gen(data[1])
gen3 = gen(data[2])
gen5 = (i for i in range(5))
res = []
def append_res(generator):
    v = next(generator)
    if not res.count(v['id']):
        res.append(v['id'])
    else:
        append_res(generator)

try:
    while True:
        next(gen5)
        append_res(gen1)
        next(gen5)
        append_res(gen2)
        next(gen5)
        append_res(gen3)
except Exception as err:
    pass
print(res)
