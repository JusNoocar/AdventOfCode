def dfs(i: int, j: int,pi: int, pj:int, a: list, used: list):
    if a[i][j] == 'I':
        print(i, j)
    used[i][j] = True
    cnt = 1
    edges = 0
    offsets = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for off in offsets:
        if (0 <= i + off[0] < len(a)) and \
           (0 <= j + off[1] < len(a[0])):
            if a[i + off[0]][j + off[1]] == a[i][j]:
                if not used[i + off[0]][j + off[1]]:
                    edges += 1
                    get = dfs(i + off[0], j + off[1], i, j, a, used)
                    cnt += get[0]
                    edges += get[1]
                else:
                    edges += 1
    return [cnt, edges]



f = open('test.txt')
data = f.readlines()
a = [[] for i in range(len(data))]
for i in range(len(data)):
    a[i] = list(data[i].strip())

used = [[False for j in range(len(a[0]))] for i in range(len(a))]

track = dict()
for i in range(len(a)):
    for j in range(len(a[i])):
        if not used[i][j]:
            get = dfs(i, j, -1, -1, a, used)
            area = get[0]
            perimeter = get[0] * 4 - get[1]
            print(a[i][j], area, perimeter)
            if a[i][j] not in track:
                track[a[i][j]] = 0
            track[a[i][j]] += area * perimeter
ans = 0
for key in track:
    ans += track[key]
print(ans)