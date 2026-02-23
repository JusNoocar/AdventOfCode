file = "test.txt"
f = open(file)
data = f.readlines()
size = len(data)
print(size)
coords = [list() for i in range(size)]
vel = [list() for i in range(size)]
for i in range(size):
    line = data[i]
    allcoords, allvel = line.split(' @ ')
    coords[i] = (list(map(int, allcoords.split(', '))))
    vel[i] = (list(map(int, allvel.split(', '))))

cnt = 0
minval = 200000000000000
maxval = 400000000000000
for i in range(size):
    for j in range(i + 1, size):
        ki = coords[i][1] - vel[i][1] * coords[i][0] / vel[i][0]
        kj = coords[j][1] - vel[j][1] * coords[j][0] / vel[j][0]
        ki1 = vel[i][1] / vel[i][0]
        kj1 = vel[j][1] / vel[j][0]
        if not((kj - ki) != 0 and (ki1 - kj1) == 0):
            x = (kj - ki) / (ki1 - kj1)
            y = ki + ki1 * x
            print(i, j)
            print(x, y)
            ti = (x - coords[i][0]) / vel[i][0]
            tj = (x - coords[j][0]) / vel[j][0]
            if (minval <= x <= maxval) and (minval <= y <= maxval) and (ti >= 0) and (tj >= 0):
                cnt += 1
                print("+1")

print(cnt)