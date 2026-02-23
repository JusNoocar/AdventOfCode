n = 101
m = 103

f = open('test.txt')
data = f.readlines()
square = [[0, 0], [0, 0]]
for line in data:
    pos, speed = [list(map(int, x[2:].split(','))) for x in line.split(' ')]
    end_pos = pos
    end_pos[0] = (pos[0] + speed[0] * 100 + n * 100) % n
    end_pos[1] = (pos[1] + speed[1] * 100 + m * 100) % m
    if end_pos[0] != (n // 2) and end_pos[1] != (m // 2):
        print(end_pos[0], end_pos[1])
        square[end_pos[0] // (n // 2 + 1)][end_pos[1] // (m // 2 + 1)] += 1

print(square)
ans = square[0][0] * square[0][1] * square[1][0] * square[1][1]
print(ans)