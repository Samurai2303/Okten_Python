import threading
# import time
# print(threading.current_thread().name)


# def show_thread(a):
#     for i in range(a):
#         time.sleep(0.5)
#         print(i, threading.current_thread().name)
#
#
# thread1 = threading.Thread(target=show_thread, args=(5,), name='thread_1')
# thread2 = threading.Thread(target=show_thread, args=(9,), name='thread_2')
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
#
# def func1(a):
#     for i in range(6):
#         time.sleep(1)
#         print(i)
#
# func1(6)
lock = threading.Lock()
count = 0
def func2():
    # with lock:
    global count
    count+=1
    print(count)

threads = []
for _ in range(100):
    thread = threading.Thread(target=func2)
    threads.append(thread)
    thread.start()
    thread.join()