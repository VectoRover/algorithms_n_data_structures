n = int(input())
seg = []
res_list = []
for _ in range(n):
    s = input()
    seg.append((int(s.split()[0]), int(s.split()[1])))
seg.sort(key=lambda x: x[1])
i = 0
res_list.append(seg[i][1])
i += 1
while i < len(seg):
    if seg[i][0] <= res_list[-1]:
        pass
    else:
        res_list.append(seg[i][1])
    i += 1


print(len(res_list))
for i in res_list:
    print(f"{i} ", end="")
