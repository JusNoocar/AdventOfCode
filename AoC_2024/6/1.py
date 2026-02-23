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
while (checker):
    a[pos_i][pos_j] = 'X'
    if direct == 0:
        if pos_i == 0:
            checker = False
        elif a[pos_i - 1][pos_j] == '#':
            direct = 1
        else:
            pos_i -= 1
    elif direct == 1:
        if pos_j == len(a[0]) - 1:
            checker = False
        elif a[pos_i][pos_j + 1] == '#':
            direct = 2
        else:
            pos_j += 1

    elif direct == 2:
        if pos_i == len(a) - 1:
            checker = False
        elif a[pos_i + 1][pos_j] == '#':
            direct = 3
        else:
            pos_i += 1

    elif direct == 3:
        if pos_j == 0:
            checker = False
        elif a[pos_i][pos_j - 1] == '#':
            direct = 0
        else:
            pos_j -= 1

cnt = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 'X':
            cnt += 1
        print(a[i][j], end='')
    print()
print(cnt)



