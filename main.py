import time
import matplotlib.pyplot as plt

cache = {}


#рекурсия без запоминания уже вычисленных значений
def fib(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


#рекурсия с запоминанием
def fib2(n):
    assert n >= 0
    if n not in cache:
        if n <= 1:
            cache[n] = n
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
    return cache[n]


#вычисление по реккурентной формуле
def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1



#вычисление по явной формуле
def fib4(n):
    assert n >= 0
    a = (1 + pow(5, 0.5) / 2)
    b = (1 - pow(5, 0.5) / 2)

    return (a**n - b**n)/pow(5, 0.5)


def timed(f, *args, n_iter=100):
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        cache.clear()
        acc = min(acc, t1 - t0)
    return acc


def work_timer(fs, args):
    for f in fs:
        if f == fib:
            args1 = list(range(15))
            plt.plot(args1, [timed(f, arg) for arg in args1], label=f.__name__)
        else:
            plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.xlabel("n")
    plt.ylabel("seconds")
    plt.legend()
    plt.grid(True)
    plt.show()


#work_timer([fib, fib2, fib3, fib4], list(range(500)))

print(fib3(3))




