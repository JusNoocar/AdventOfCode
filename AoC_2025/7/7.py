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
ops = [0 for i in range(n * m)]
cnt = 0
splits = 0
def dfs(v: int):
    global used
    global cnt
    global splits
    used[v] = True
    print (v // m, v % m)
    check = 0
    if len(g[v]) > 1:
        splits += 1
    for u in g[v]:
        if u == -1:
            ops[v] = 1
            cnt += 1
        else:
          if not used[u]:
            dfs(u)
          ops[v] += ops[u]

dfs(start)
print(ops[start])
print(cnt)
print(splits)


