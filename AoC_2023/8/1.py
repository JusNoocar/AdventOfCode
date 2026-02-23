file = open('test.txt','r')
data = file.readlines()
#print(data)

path = data[0][:-1]
#print(path)
g = dict()
for i in range(2, len(data)):
    v, u1_u2 = data[i].split(' = ')
    if i == len(data) - 1:
        u1, u2 = u1_u2[1: -1].split(', ')
    else:
        u1, u2 = u1_u2[1: -2].split(', ')
    g[v] = [u1, u2]
    #print(v, u1, u2)

v = 'AAA'
ans = -1
for i in range(1000000):
    
    idx = i % len(path)
    if path[idx] == 'L':
        v = g[v][0]
    else:
        v = g[v][1]
    #print(v)
    if v == 'ZZZ':
        ans = i
        break

print(ans + 1)