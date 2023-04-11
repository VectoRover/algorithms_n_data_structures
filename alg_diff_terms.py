"""
По данному числу найдите максимальное число k, для которого 
n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых

решение через жадный алгоритм
добавляем к сумме числа, до тех пор, пока она не превысит n, потом удаляем
из списка одно число- то, на которое превысили
"""

def diff_terms(n):
    if n == 1:
        print('1')
        print('1')
        return

    terms = []
    k = 0
    sm = 0

    for i in range(1, n + 1):
        sm += i
        terms.append(i)
        if sm > n:
            target = sm - n
            terms.pop(target - 1)
            break
    print(len(terms))
    for i in terms:
        print(i, end='')
        print(" ", end = '')
    return

diff_terms(12)
