"""
Первая строка содержит количество предметов и вместимость рюкзака. Каждая из следующих 
n строк задаёт стоимость и объём предмета.
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость
и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.
"""

s = input()
n = int(s.split()[0])
W = int(s.split()[1])
d = []
for i in range(n):
    s = input()
    d.append((int(s.split()[0]), int(s.split()[1])))
d = sorted(d, key = lambda x:x[0] / x[1], reverse = True)
sum = 0
for i in range(n):
    if  W < 1e-5:
        break
    else:
        if d[i][1] < W:
            sum += d[i][0]
            W -= d[i][1]
        else:
            sum += W * d[i][0] / d[i][1]
            W = 0
print('%.3f' % sum)


