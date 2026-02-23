
def move_left(pos: list):
    global a
    if a[pos[0]][pos[1]] in ['.', '#'] or pos[1] == 0:
        return [pos[0], pos[1]]
    move_left([pos[0], pos[1] - 1])
    if a[pos[0]][pos[1] - 1] == '.':
        a[pos[0]][pos[1] - 1] = a[pos[0]][pos[1]]
        a[pos[0]][pos[1]] = '.'
        return [pos[0], pos[1] - 1]

    return [pos[0], pos[1]]

def move_right(pos: list):
    global a
    if a[pos[0]][pos[1]] in ['.', '#'] or pos[1] == len(a[0]) - 1:
        return [pos[0], pos[1]]
    move_right([pos[0], pos[1] + 1])
    if a[pos[0]][pos[1] + 1] == '.':
        a[pos[0]][pos[1] + 1] = a[pos[0]][pos[1]]
        a[pos[0]][pos[1]] = '.'
        return [pos[0], pos[1] + 1]

    return [pos[0], pos[1]]

def move_up(pos: list):
    global a
    if a[pos[0]][pos[1]] in ['.', '#'] or pos[0] == 0:
        return [pos[0], pos[1]]
    move_up([pos[0] - 1, pos[1]])
    if a[pos[0] - 1][pos[1]] == '.':
        a[pos[0] - 1][pos[1]] = a[pos[0]][pos[1]]
        a[pos[0]][pos[1]] = '.'
        return [pos[0] - 1, pos[1]]

    return [pos[0], pos[1]]

def move_down(pos: list):
    global a
    if a[pos[0]][pos[1]] in ['.', '#'] or pos[0] == len(a) - 1:
        return [pos[0], pos[1]]
    move_down([pos[0] + 1, pos[1]])
    if a[pos[0] + 1][pos[1]] == '.':
        a[pos[0] + 1][pos[1]] = a[pos[0]][pos[1]]
        a[pos[0]][pos[1]] = '.'
        return [pos[0] + 1, pos[1]]

    return [pos[0], pos[1]]




f = open('test.txt')
data = f.readlines()
a = []
line_id = 1
while data[line_id] != '\n':
    line = data[line_id].strip()
    if line != len(line) * '#':
        a.append([])
        a[-1] = list(line[1:-1])
    line_id += 1

pos = [0, 0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == '@':
            pos = [i, j]

line_id += 1
while line_id < len(data):
    line = data[line_id].strip()
    for arrow in line:
        match arrow:
            case '^':
                pos = move_up(pos)
            case '>':
                pos = move_right(pos)
            case '<':
                pos = move_left(pos)
            case 'v':
                pos = move_down(pos)
    line_id += 1


ans = 0
print((len(a[0]) + 2) * '#')
for i in range(len(a)):
    print('#', end='')
    for j in range(len(a[i])):
        print(a[i][j], end='')
        if a[i][j] == 'O':
            ans += 100 * (i + 1) + (j + 1)
    print('#')
print((len(a[0]) + 2) * '#')
print(ans)

