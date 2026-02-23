def walk(a, pos_i, pos_j):
    checker = True
    direct = 0
    dirs = dict()
    m = len(a[0])
    loop = False
    while checker:
        #a[pos_i][pos_j] = 'X'
        if direct == 0:
            if pos_i == 0:
                checker = False
            elif a[pos_i - 1][pos_j] == '#':
                direct = 1
                if (pos_i - 1) * m + pos_j in dirs and dirs[(pos_i - 1) * m + pos_j] == 0:
                    loop = True
                    checker = False
                dirs[(pos_i - 1) * m + pos_j] = 0
            else:
                pos_i -= 1
        elif direct == 1:
            if pos_j == len(a[0]) - 1:
                checker = False
            elif a[pos_i][pos_j + 1] == '#':
                direct = 2
                if pos_i * m + pos_j + 1 in dirs and dirs[pos_i * m + pos_j + 1] == 1:
                    loop = True
                    checker = False
                dirs[pos_i * m + pos_j + 1] = 1
            else:
                pos_j += 1

        elif direct == 2:
            if pos_i == len(a) - 1:
                checker = False
            elif a[pos_i + 1][pos_j] == '#':
                direct = 3
                if (pos_i + 1) * m + pos_j in dirs and dirs[(pos_i + 1) * m + pos_j] == 2:
                    loop = True
                    checker = False
                dirs[(pos_i + 1) * m + pos_j] = 2
            else:
                pos_i += 1

        elif direct == 3:
            if pos_j == 0:
                checker = False
            elif a[pos_i][pos_j - 1] == '#':
                direct = 0
                if pos_i * m + pos_j - 1 in dirs and dirs[pos_i * m + pos_j - 1] == 3:
                    loop = True
                    checker = False
                dirs[pos_i * m + pos_j - 1] = 3
            else:
                pos_j -= 1
    return loop

f = open('test.txt')
data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].strip()
pos_i = -1
pos_j = -1
a = [['' for j in range(len(data[0]))] for i in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[0])):
        a[i][j] = data[i][j]
        if a[i][j] == '^':
            pos_i = i
            pos_j = j

cuties = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == '.':
            a[i][j] = '#'
            if walk(a, pos_i, pos_j):
                cuties += 1
            a[i][j] = '.'



cnt = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 'X':
            cnt += 1
        print(a[i][j], end='')
    print()
print(cnt)
print(cuties)



