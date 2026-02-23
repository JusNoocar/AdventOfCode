f = open('test.txt')
data = f.readlines()
rules = []
step = 0

ans = 0
not_sorted = []
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
        if not checker:
            not_sorted.append([])
            not_sorted[-1] = a

'''
seconds = [rule[1] for rule in rules]
starts = []
g = [[] for i in range(100)]
for rule in rules:
    if (rule[0] not in seconds) and (rule[0] not in starts):
        starts.append(rule)
    g[rule[0]].
'''
ans = 0
for a in not_sorted:
    ind = dict()
    for i in range(len(a)):
        ind[a[i]] = i
    checker = False
    while not checker:
        checker = True
        for [v, u] in rules:
            if (v in ind) and (u in ind) and ind[v] > ind[u]:
                checker = False
                a[ind[v]], a[ind[u]] = a[ind[u]], a[ind[v]]
                ind[v], ind[u] = ind[u], ind[v]
    m = len(a) // 2
    ans += a[m]

print(ans)