import threading


# <editor-fold desc="创建线程">

def loop():
    print("Hello world")
    print("当前线程%s" % threading.current_thread().name)


t1 = threading.Thread(target=loop, name="loop-thread")

t1.start()

t1.join()

print("当前线程%s" % threading.current_thread().name)

# </editor-fold>


# <editor-fold desc="多线程-无锁">
balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(10000,))
t2 = threading.Thread(target=run_thread, args=(6330,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)

# </editor-fold>

# <editor-fold desc="多线程-锁">

balance = 9
lock = threading.Lock()


def change_b(m):
    global balance
    balance = balance + m
    balance = balance - m


def run_change(n):
    for i in range(100000):
        try:
            # 获取锁
            lock.acquire()
            change_b(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_change, args=(987,))
t2 = threading.Thread(target=run_change, args=(9800,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)

# </editor-fold>

# <editor-fold desc="ThreadLocal">

local = threading.local()


# </editor>
