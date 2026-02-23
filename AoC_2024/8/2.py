f = open('test.txt')
data = f.readlines()
freq = dict()
for i in range(len(data)):
    data[i] = data[i].strip()
    for j in range(len(data[i])):
        if data[i][j] != '.':
            if data[i][j] not in freq:
                freq[data[i][j]] = []
            freq[data[i][j]].append([i, j])

field = [['.' for j in range(len(data[0]))] for i in range(len(data))]
for f in freq:
    for p1 in range(len(freq[f])):
        for p2 in range(p1 + 1, len(freq[f])):
            i1, j1 = freq[f][p1]
            i2, j2 = freq[f][p2]
            field[i1][j1] = '#'
            field[i2][j2] = '#'
            if j1 > j2:
                i1, i2 = i2, i1
                j1, j2 = j2, j1

            i3, j3 = i2 + (i2 - i1), j2 + (j2 - j1)
            i4, j4 = i1 - (i2 - i1), j1 - (j2 - j1)
            while 0<=i3<len(field) and 0<=j3<len(field[0]):
                field[i3][j3] = '#'
                i3 += (i2 - i1)
                j3 += (j2 - j1)

            while 0<=i4<len(field) and 0<=j4<len(field[0]):
                field[i4][j4] = '#'
                i4 -= (i2 - i1)
                j4 -= (j2 - j1)
ans = 0
for i in range(len(field)):
    for j in range(len(field[0])):
        print(field[i][j],end='')
        if field[i][j] == '#':
            ans += 1
    print()

print(ans)

