import math
import multiprocessing
import time

def time_decor(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(time.time()-start_time)
    return inner

def hard_operation(number:int):
    return str(math.sqrt(math.sqrt(math.sqrt(math.sqrt(number*7364/34/3/5*224)))))+'asd'


@time_decor
def main_func():
    print('Main')
    with open('file1.txt', 'w') as file:
        for i in range(10000000):
            res = hard_operation(i)
            print(res, file=file)

# main_func()


# @time_decor
# def main_func_mp():
#     print('mp')
#     count = multiprocessing.cpu_count()
#     print(count, 'CPUs')
#     with multiprocessing.Pool(6) as p :
#         with open('file.txt', 'w') as file:
#             res = p.map(hard_operation, range(10000000))
#             for i in res:
#                 print(i, file=file)

# main_func_mp()
# Not working...
