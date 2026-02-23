with open("7.txt") as f:
    a = [line.strip() for line in f.readlines()]
n = len(a)
m = len(a[0])
g = [[] for i in range(n * m)]
start = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            start = i * m + j
        if (a[i][j] == '.' or a[i][j] == 'S') and i < n - 1:
            g[i * m + j].append((i + 1) * m + j)
        elif (a[i][j] == '.' or a[i][j] == 'S') and i == n - 1:
            g[i * m + j].append(-1)
        elif a[i][j] == '^':
            if j > 0:
                g[i * m + j].append(i * m + j - 1)
            if j < m - 1:
                g[i * m + j].append(i * m + j + 1)

used = [False for i in range(n * m)]
cnt = 0
splits = 0
ans = 0

queue = [start]
ops = [0 for i in range(n * m)]
ops[start] = 1
while len(queue) != 0:
    v = queue[0]
    queue.pop(0)
    used[v] = True
    print (v // m, v % m)
    if len(g[v]) > 1:
        splits += 1
    for u in g[v]:
        if u == -1:
            cnt += 1
            ans += ops[v]
        else:
            ops[u] += ops[v]
            if not used[u] and u not in queue:
                pass
            queue.append(u)

print(cnt)
print(splits)
print(ans)


