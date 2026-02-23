import functools

def cmp(a, b):
    return a[0][2] < b[0][2]

def intersect(a, b):
    if min(a[1][0], b[1][0]) >= max(a[0][0], b[0][0]) and min(a[1][1], b[1][1]) >= max(a[0][1], b[0][1]):
        return True
    return False
f = open('test.txt', 'r')

a = [line.strip() for line in f.readlines()]

bricks = [[] for i in range(len(a))]

for i in range(len(a)):
    line = a[i]
    coords1, coords2 = line.split('~')

    p1 = list(map(int, coords1.split(',')))
    p2 = list(map(int, coords2.split(',')))
    bricks[i] = [p1, p2, i]

bricks = sorted(bricks, key=functools.cmp_to_key(cmp))


for i in range(len(bricks)):
    bound = 0
    for j in range(len(bricks)):
        if i == j:
            continue
        if bricks[j][1][2] < bricks[i][0][2] and intersect(bricks[i], bricks[j]):
            bound = max(bound, bricks[j][1][2] + 1)
    prev = bricks[i][0][2]
    bricks[i][1][2] = bricks[i][1][2] - (bricks[i][0][2] - bound)
    bricks[i][0][2] = bound
    print(i, 'fell from', prev, 'to', bricks[i][0][2])
            
