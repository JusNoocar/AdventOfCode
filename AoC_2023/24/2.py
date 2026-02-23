
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
p1 = [0 for i in range(3)]
p2 = [0 for i in range(3)]
v1 = [0 for i in range(3)]
v2 = [0 for i in range(3)]
for i in range(3):
    p1[i] = coords[1][i] - coords[0][i]
    p2[i] = coords[2][i] - coords[0][i]
    v1[i] = vel[1][i] - vel[0][i]
    v2[i] = vel[2][i] - vel[0][i]

def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], -(a[0] * b[2] - a[2] * b[0]), a[0] * b[1] - a[1] * b[0]]
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


t1 = -(dot(cross(p1, p2), v2)) / (dot(cross(v1, p2), v2))
t2 = -(dot(cross(p1, p2), v1)) / (dot(cross(p1, v2), v1))

ans = 0
for i in range(3):
    c1 = coords[1][i] + t1 * vel[1][i]
    c2 = coords[2][i] + t2 * vel[2][i]
    v = (c2 - c1) / (t2 - t1)
    pos = c1 - t1 * v
    print(pos)
    ans += pos

print(ans)

