
def search(a:list, i:int, j:int):
    if a[i][j] == 9:
        global pos9
        hsh = i * len(a[0]) + j
        pos9.add(hsh)
        #print('+1')
    offsets = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for off in offsets:
        if (0 <= i + off[0] < len(a)) and \
           (0 <= j + off[1] < len(a[0])):
            if (a[i + off[0]][j + off[1]] - a[i][j]) == 1:
                search(a, i + off[0], j + off[1])


f = open('test.txt')
data = f.readlines()
a = [[] for i in range(len(data))]
for i in range(len(data)):
    data[i] = data[i].strip()
    a[i] = list(map(int, list(data[i])))
print(len(a), len(a[0]))
ans = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 0:
            #print('start')
            pos9 = set()
            search(a, i, j)
            ans += len(pos9)

print(ans)


