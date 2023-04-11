import heapq
import time
import matplotlib.pyplot as plt
import random
import string
from collections import Counter, deque
s = input()


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def timed(f, *args, n_iter=10):
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def huffman_encoder(s):
    res = {}
    stack = deque()
    code = {}
    h = [(i[1], i[0]) for i in Counter(s).items()]
    if len(h) == 1:
        return {h[0][1]: '0'}, h[0][0] * '0'
    heapq.heapify(h)
    while len(h) > 1:
        fr1, el1 = heapq.heappop(h)
        fr2, el2 = heapq.heappop(h)
        heapq.heappush(h, (fr1 + fr2, el1 + el2))
        res[el1 + el2] = (el1, el2)
        stack.append(el1 + el2)
    #k = stack.pop()
    #stack.append(k)
    code[stack[-1]] = ""
    for key in res:
        code[res[key][0]] = ""
        code[res[key][1]] = ""
    for i in range(len(stack)):
        t = stack.pop()
        code[res[t][0]] += code[t] + '0'
        code[res[t][1]] += code[t] + '1'
    code_string = ""
    for i in s:
        code_string += code[i]
    return code, code_string


def work_timer(f, args):
    Y = [timed(f, arg) for arg in args]
    X = [len(arg) for arg in args]
    plt.plot(X, Y, label=f.__name__)
    plt.xlabel("n")
    plt.ylabel("seconds")
    plt.legend()
    plt.grid(True)
    plt.show()

code, res = huffman_encoder(s)
print(len([i for i in Counter(s).items()]), len(res))
for i in set(s):
    print(i + ": " + str(code[i]))
    pass
print(res)


work_timer(huffman_encoder, [generate_random_string(i) for i in range(1, 10000)])



