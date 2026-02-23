def side_counter(i: int, j: int, a: list):
    cnt = 0

    if (j == 0 or a[i][j - 1] != a[i][j]) and (i == 0 or a[i - 1][j] != a[i][j]):
        cnt += 1
    elif (i != 0 and a[i - 1][j] != a[i][j]) and (j != 0 and a[i - 1][j - 1] == a[i][j]):
        cnt += 1
    if (j == 0 or a[i][j - 1] != a[i][j]) and (i == len(a) - 1 or a[i + 1][j] != a[i][j]):
        cnt += 1
    elif (i != len(a) - 1 and a[i + 1][j] != a[i][j]) and (j != 0 and a[i + 1][j - 1] == a[i][j]):
        cnt += 1

    if (j == 0 or a[i][j - 1] != a[i][j]) and (i == 0 or a[i - 1][j] != a[i][j]):
        cnt += 1
    elif (j != 0 and a[i][j - 1] != a[i][j]) and (i != 0 and a[i - 1][j - 1] == a[i][j]):
        cnt += 1
    if (j == len(a[i]) - 1 or a[i][j + 1] != a[i][j]) and (i == 0 or a[i - 1][j] != a[i][j]):
        cnt += 1
    elif (j != len(a[i]) - 1 and a[i][j + 1] != a[i][j]) and (i != 0 and a[i - 1][j + 1] == a[i][j]):
        cnt += 1
    return cnt


def dfs(i: int, j: int, pi: int, pj:int, a: list, used: list):
    used[i][j] = True
    cnt = 1
    sides = side_counter(i, j, a)
    offsets = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for off in offsets:
        if (0 <= i + off[0] < len(a)) and \
           (0 <= j + off[1] < len(a[0])):
            if a[i + off[0]][j + off[1]] == a[i][j]:
                if not used[i + off[0]][j + off[1]]:
                    get = dfs(i + off[0], j + off[1], i, j, a, used)
                    cnt += get[0]
                    sides += get[1]

    return [cnt, sides]



f = open('test.txt')
data = f.readlines()
a = [[] for i in range(len(data))]
for i in range(len(data)):
    a[i] = list(data[i].strip())

used = [[False for j in range(len(a[0]))] for i in range(len(a))]
b = [[0 for j in range(len(a[0]))] for i in range(len(a))]
idx = 0

ans = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if not used[i][j]:
            get = dfs(i, j, -1, -1, a, used)
            ans += get[0] * get[1]
print(ans)