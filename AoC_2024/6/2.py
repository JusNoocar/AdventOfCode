f = open('test.txt')
data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].strip()
direct = 0
pos_i = -1
pos_j = -1
a = [['' for j in range(len(data[0]))] for i in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[0])):
        a[i][j] = data[i][j]
        if a[i][j] == '^':
            pos_i = i
            pos_j = j

checker = True
dirs = dict()
cuties = 0
m = len(a[0])
while (checker):
    a[pos_i][pos_j] = 'X'
    if direct == 0:
        if pos_i == 0:
            checker = False
        elif a[pos_i - 1][pos_j] == '#':
            direct = 1
            dirs[(pos_i - 1) * m + pos_j] = 0
        else:
            for j in range(pos_j + 1, len(a[0])):
                if a[pos_i][j] == '#':
                    cup = pos_i * m + j
                    if cup in dirs and dirs[cup] == 1:
                        cuties += 1
                        print(pos_i - 1, pos_j)
                    break
            pos_i -= 1
    elif direct == 1:
        if pos_j == len(a[0]) - 1:
            checker = False
        elif a[pos_i][pos_j + 1] == '#':
            direct = 2
            dirs[pos_i * m + pos_j + 1] = 1
        else:
            for i in range(pos_i + 1, len(a)):
                if a[i][pos_j] == '#':
                    cup = i * m + pos_j
                    if cup in dirs and dirs[cup] == 2:
                        cuties += 1
                        print(pos_i, pos_j + 1)
                    break
            pos_j += 1

    elif direct == 2:
        if pos_i == len(a) - 1:
            checker = False
        elif a[pos_i + 1][pos_j] == '#':
            direct = 3
            dirs[(pos_i + 1) * m + pos_j] = 2
        else:
            for j in range(pos_j - 1, -1, -1):
                if a[pos_i][j] == '#':
                    cup = pos_i * m + j
                    if cup in dirs and dirs[cup] == 3:
                        cuties += 1
                        print(pos_i + 1, pos_j)
                    break
            pos_i += 1

    elif direct == 3:
        if pos_j == 0:
            checker = False
        elif a[pos_i][pos_j - 1] == '#':
            direct = 0
            dirs[pos_i * m + pos_j - 1] = 3
        else:
            for i in range(pos_i - 1, -1, -1):
                if a[i][pos_j] == '#':
                    cup = i * m + pos_j
                    if cup in dirs and dirs[cup] == 0:
                        cuties += 1
                        print(pos_i, pos_j - 1)
                    break
            pos_j -= 1

cnt = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 'X':
            cnt += 1
        print(a[i][j], end='')
    print()
print(cnt)
print(cuties)



