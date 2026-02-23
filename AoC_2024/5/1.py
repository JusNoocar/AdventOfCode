f = open('test.txt')
data = f.readlines()
rules = []
step = 0

ans = 0
for line in data:
    if line == '\n':
        step = 1
        continue
    line = line.strip()
    if step == 0:
        v, u = map(int, line.split('|'))
        rules.append([])
        rules[-1] = [v, u]
    else:
        checker = True
        a = list(map(int, line.split(',')))
        ind = dict()
        for i in range(len(a)):
            ind[a[i]] = i
        for [v, u] in rules:
            if (v in ind) and (u in ind) and ind[v] > ind[u]:
                checker = False
        if checker:
            m = len(a) // 2
            ans += a[m]

print(ans)