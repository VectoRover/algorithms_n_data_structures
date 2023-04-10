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