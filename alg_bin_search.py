"""
итеративный алгоритм бинарного поиска
bin search получает ключ и отсортированный массив и возвращает индекс ключа,
если он есть в массиве и -1, если его нет

работает за лог время
"""


s = input().split()
n = int(s[0])
A = list(map(int, s[1: ]))

s = input().split()
k = int(s[0])
B = list(map(int, s[1: ]))


def BinSearch(target, A):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = l + (r - l) // 2
        if A[m] == target:
            return m
        else:
            if target < A[m]:
                r = m - 1
            else:
                l = m + 1
    return -2


res = []
for i in B:
    res.append(BinSearch(i, A) + 1)
for i in res:
    print(i, " ", end = '')




