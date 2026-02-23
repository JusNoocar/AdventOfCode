import os
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

def check_up(pos: list):
    global a
    if a[pos[0]][pos[1]] == '#':
        return False
    if a[pos[0]][pos[1]] == '.':
        return True
    if pos[0] == 0:
        return False
    if a[pos[0]][pos[1]] == '@':
        if check_up([pos[0] - 1, pos[1]]):
            return True
        return False

    if a[pos[0]][pos[1]] == '[':
        if check_up([pos[0] - 1, pos[1]]) and check_up([pos[0] - 1, pos[1] + 1]):
            return True
        return False

    if a[pos[0]][pos[1]] == ']':
        if check_up([pos[0] - 1, pos[1]]) and check_up([pos[0] - 1, pos[1] - 1]):
            return True
        return False
def move_up(pos: list):
    global a
    if a[pos[0]][pos[1]] in ['.', '#'] or pos[0] == 0:
        return [pos[0], pos[1]]

    if a[pos[0]][pos[1]] == '@' and check_up([pos[0] - 1, pos[1]]):
        move_up([pos[0] - 1, pos[1]])
        a[pos[0] - 1][pos[1]] = a[pos[0]][pos[1]]
        a[pos[0]][pos[1]] = '.'
        return [pos[0] - 1, pos[1]]

    if a[pos[0]][pos[1]] == '[':
        if check_up([pos[0] - 1, pos[1]]) and check_up([pos[0] - 1, pos[1] + 1]):
            move_up([pos[0] - 1, pos[1]])
            move_up([pos[0] - 1, pos[1] + 1])
            a[pos[0] - 1][pos[1]] = a[pos[0]][pos[1]]
            a[pos[0] - 1][pos[1] + 1] = a[pos[0]][pos[1] + 1]
            a[pos[0]][pos[1]] = '.'
            a[pos[0]][pos[1] + 1] = '.'
            return [pos[0] - 1, pos[1]]

    if a[pos[0]][pos[1]] == ']':
        if check_up([pos[0] - 1, pos[1]]) and check_up([pos[0] - 1, pos[1] - 1]):
            move_up([pos[0] - 1, pos[1] - 1])
            move_up([pos[0] - 1, pos[1]])
            a[pos[0] - 1][pos[1]] = a[pos[0]][pos[1]]
            a[pos[0] - 1][pos[1] - 1] = a[pos[0]][pos[1] - 1]
            a[pos[0]][pos[1]] = '.'
            a[pos[0]][pos[1] - 1] = '.'
            return [pos[0] - 1, pos[1]]

    return [pos[0], pos[1]]

def check_down(pos: list):
    global a
    if a[pos[0]][pos[1]] == '#':
        return False
    if a[pos[0]][pos[1]] == '.':
        return True
    if pos[0] == len(a) - 1:
        return False
    if a[pos[0]][pos[1]] == '@':
        if check_down([pos[0] + 1, pos[1]]):
            return True
        return False

    if a[pos[0]][pos[1]] == '[':
        if check_down([pos[0] + 1, pos[1]]) and check_down([pos[0] + 1, pos[1] + 1]):
            return True
        return False

    if a[pos[0]][pos[1]] == ']':
        if check_down([pos[0] + 1, pos[1]]) and check_down([pos[0] + 1, pos[1] - 1]):
            return True
        return False

def move_down(pos: list):
    global a
    if a[pos[0]][pos[1]] in ['.', '#'] or pos[0] == len(a) - 1:
        return [pos[0], pos[1]]



    if a[pos[0]][pos[1]] == '@' and check_down([pos[0] + 1,pos[1]]):
        move_down([pos[0] + 1, pos[1]])
        a[pos[0] + 1][pos[1]] = a[pos[0]][pos[1]]
        a[pos[0]][pos[1]] = '.'
        return [pos[0] + 1, pos[1]]

    if a[pos[0]][pos[1]] == '[':

        if check_down([pos[0] + 1, pos[1]]) and check_down([pos[0] + 1, pos[1] + 1]):
            move_down([pos[0] + 1, pos[1]])
            move_down([pos[0] + 1, pos[1] + 1])
            a[pos[0] + 1][pos[1]] = a[pos[0]][pos[1]]
            a[pos[0] + 1][pos[1] + 1] = a[pos[0]][pos[1] + 1]
            a[pos[0]][pos[1]] = '.'
            a[pos[0]][pos[1] + 1] = '.'
            return [pos[0] + 1, pos[1]]

    if a[pos[0]][pos[1]] == ']':

        if check_down([pos[0] + 1, pos[1]]) and check_down([pos[0] + 1, pos[1] - 1]):
            move_down([pos[0] + 1, pos[1] - 1])
            move_down([pos[0] + 1, pos[1]])
            a[pos[0] + 1][pos[1]] = a[pos[0]][pos[1]]
            a[pos[0] + 1][pos[1] - 1] = a[pos[0]][pos[1] - 1]
            a[pos[0]][pos[1]] = '.'
            a[pos[0]][pos[1] - 1] = '.'
            return [pos[0] + 1, pos[1]]

    return [pos[0], pos[1]]

def display():
    global a
    s = ''
    for i in range(len(a)):
        s += ''.join(a[i])
        if i != len(a) - 1:
            s += '\n'
    os.system('cls')
    print(s, end='\r')




f = open('test.txt')
data = f.readlines()
a = []
line_id = 1
while data[line_id] != '\n':
    line = data[line_id].strip()
    if line != len(line) * '#':
        a.append([])
        line = line[1:-1]
        for i in range(len(line)):
            if line[i] == '@':
                a[-1].append('@')
                a[-1].append('.')
            elif line[i] == 'O':
                a[-1].append('[')
                a[-1].append(']')
            else:
                a[-1].append(line[i])
                a[-1].append(line[i])
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
        #display()
    line_id += 1


ans = 0
print((len(a[0]) + 4) * '#')
for i in range(len(a)):
    print('##', end='')
    for j in range(len(a[i])):
        print(a[i][j], end='')
        if a[i][j] == '[':
            ans += 100 * (i + 1) + j + 2
    print('##')
print((len(a[0]) + 4) * '#')
print(ans)


#for i in range(len(a)):
#    for j in range(len(a[i])):
#        if a[i][j] == '[':
#            print(min(i + 1, len(a) - i), min(j + 1, len(a[i]) - j - 1) + 1)

