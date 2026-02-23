n = 101
m = 103

f = open('test.txt')
data = f.readlines()

pos = [[] for i in range(len(data))]
speed = [[] for i in range(len(data))]
field = [[0 for j in range(103)] for i in range(101)]
for i in range(len(data)):
    line = data[i]
    pos[i], speed[i] = [list(map(int, x[2:].split(','))) for x in line.split(' ')]
    field[pos[i][0]][pos[i][1]] += 1

for t in range(100000):
    for i in range(len(data)):
        field[pos[i][0]][pos[i][1]] -= 1
        end_pos = pos[i]
        end_pos[0] = (pos[i][0] + speed[i][0] + 20 * n) % n
        end_pos[1] = (pos[i][1] + speed[i][1] + 20 * m) % m
        pos[i] = end_pos
        field[pos[i][0]][pos[i][1]] += 1

    count = 0
    xs = set()
    ys = set()
    for x in range(101):
        for y in range(103):
            if field[x][y] == 1:
                count += 1
            if field[x][y] > 0:
                xs.add(x)
                ys.add(y)

    if count == 500:
        print(t)
        for x in range(101):
            for y in range(103):
                if field[x][y] > 0:
                    print('*', end='')
                else:
                    print('.', end='')
            print()
        print()
        print()

    '''
    for i in range(len(data)):
        if pos[i][1] > 1 and pos[i][0] < 99 and pos[i][1] < 101:
            if field[pos[i][0] + 1][pos[i][1] - 1] > 0:
                if field[pos[i][0] + 2][pos[i][1] - 2] > 0:
                    if field[pos[i][0] + 1][pos[i][1] + 1] > 0:
                        if field[pos[i][0] + 2][pos[i][1] + 2] > 0:
                            print(t, ': ')
    '''

