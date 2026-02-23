with open("4.txt") as f:
    data = [[x for x in line.strip()] for line in f.readlines()]
print(data)
cnt = 0
n = len(data)
m = len(data[0])
que = []

save = [[-1 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] != '@':
            continue
        c = 0
        
        if (i > 0):
            c += 1 if data[i - 1][j] == '@' else 0
            c += 1 if j > 0 and data[i - 1][j - 1] == '@' else 0
            c += 1 if j < m - 1 and data[i - 1][j + 1] == '@' else 0

        if (i < n - 1):
            c += 1 if data[i + 1][j] == '@' else 0
            c += 1 if j > 0 and data[i + 1][j - 1] == '@' else 0
            c += 1 if j < m - 1 and data[i + 1][j + 1] == '@' else 0

        c += 1 if j > 0 and data[i][j - 1] == '@' else 0
        c += 1 if j < m - 1 and data[i][j + 1] == '@' else 0

        save[i][j] = c
        if c < 4:
          cnt += 1
          que.append((i, j))

used = []
while len(que) != 0:
    i, j = que[0]

    que.pop(0)
    used.append((i, j))
    data[i][j] = '.'
    for i1 in range(max(0, i - 1), min(n - 1, i + 1) + 1):
        for j1 in range(max(0, j - 1), min(m - 1, j + 1) + 1):
            if i1 == i and j1 == j:
                continue
            if data[i1][j1] == '@':
                save[i1][j1] -= 1
                if save[i1][j1] < 4 and (i1, j1) not in used and (i1, j1) not in que:
                    cnt += 1
                    que.append((i1, j1))

print('\n'.join([''.join(x) for x in data]))
    



print(cnt)
